import os
import sys
import fitz  # PyMuPDF
from PIL import Image

# Folder paths
INPUT_DIR = "input slides"
OUTPUT_DIR = "output slides"

os.makedirs(OUTPUT_DIR, exist_ok=True)

DPI = 200  # safer than 300


def split_pdf_into_slides(input_pdf_path, output_pdf_path):
    try:
        pdf = fitz.open(input_pdf_path)
        slide_images = []

        total_pages = len(pdf)
        slide_count = 0

        for page_number in range(total_pages):
            print(f"  Page {page_number + 1}/{total_pages}")

            page = pdf[page_number]
            pix = page.get_pixmap(dpi=DPI)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

            width, height = img.size

            regions = [
                (0, 0, width // 2, height // 2),
                (width // 2, 0, width, height // 2),
                (0, height // 2, width // 2, height),
                (width // 2, height // 2, width, height),
            ]

            for region in regions:
                slide = img.crop(region)
                slide_images.append(slide)
                slide_count += 1
                print(f"    Slide {slide_count}")

            # cleanup
            img.close()
            pix = None

        print(f"  Saving {slide_count} slides...")
        slide_images[0].save(
            output_pdf_path,
            save_all=True,
            append_images=slide_images[1:]
        )

        for s in slide_images:
            s.close()

        print("  ✅ Done")

    except MemoryError:
        print("\n❌ Not enough memory. Try closing other applications.")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


# ================= MAIN =================

print("🚀 Slide conversion started\n")

for file_name in os.listdir(INPUT_DIR):
    if file_name.lower().endswith(".pdf"):
        print(f"📄 Processing: {file_name}")

        input_path = os.path.join(INPUT_DIR, file_name)
        base_name = os.path.splitext(file_name)[0]
        output_name = f"{base_name}_slide_adjusted.pdf"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        split_pdf_into_slides(input_path, output_path)
        print(f"📁 Saved as: {output_name}\n")

print("🎉 All PDFs processed successfully!")