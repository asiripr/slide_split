import os
import fitz  # PyMuPDF
from PIL import Image

# Folder paths
INPUT_DIR = "input slides"
OUTPUT_DIR = "output slides"

# Create output folder if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_pdf_into_slides(input_pdf_path, output_pdf_path):
    pdf = fitz.open(input_pdf_path)
    slide_images = []

    for page_number in range(len(pdf)):
        page = pdf[page_number]
        pix = page.get_pixmap(dpi=300)  # high quality
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        width, height = img.size

        # Define 4 slide regions (2x2)
        regions = [
            (0, 0, width // 2, height // 2),
            (width // 2, 0, width, height // 2),
            (0, height // 2, width // 2, height),
            (width // 2, height // 2, width, height),
        ]

        for region in regions:
            slide = img.crop(region)
            slide_images.append(slide)

    # Save all slides into one PDF (1 slide per page)
    slide_images[0].save(
        output_pdf_path,
        save_all=True,
        append_images=slide_images[1:]
    )

# Loop through all PDFs in input folder
for file_name in os.listdir(INPUT_DIR):
    if file_name.lower().endswith(".pdf"):
        input_path = os.path.join(INPUT_DIR, file_name)

        base_name = os.path.splitext(file_name)[0]
        output_name = f"{base_name}_slide_adjusted.pdf"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        print(f"Processing: {file_name}")
        split_pdf_into_slides(input_path, output_path)
        print(f"Saved as: {output_name}")

print("\n✅ All PDFs processed successfully!")
