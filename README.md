# 📄 PDF Slide Splitter

Convert lecture PDFs with **4 slides per page** into a clean PDF where **each page contains exactly one slide**.

Ideal for students, researchers, and lecturers who receive handout-style slides and want a more readable format.

---

## ✨ Features

- ✅ Converts **4 slides per page → 1 slide per page**
- ✅ Batch processes **multiple PDF files**
- ✅ Shows **real-time progress** in the terminal
- ✅ Optimized for **low-performance PCs**
- ✅ **Beginner-friendly** and easy to modify
- ✅ Generates **clean and readable** output PDFs

---

## 📁 Project Structure

Create the following folder structure before running the script:

```
project-folder/
├── input slides/
│   ├── lec 01 topic.pdf
│   ├── lec 02 ontology.pdf
│   └── ... (add your PDFs here)
├── output slides/
│   └── (converted PDFs will appear here automatically)
└── split_slides.py
```

**Instructions:**
- Place your original PDFs inside **`input slides/`**
- Converted PDFs will be saved automatically in **`output slides/`**

---

## 🛠️ Requirements

### Python Version
- Python **3.8 or higher** is required

Check your Python version:
```bash
python --version
```

### Required Libraries

Install the necessary packages using pip:

```bash
pip install pymupdf pillow
```

**Package details:**
- `pymupdf` (PyMuPDF) - PDF manipulation library
- `pillow` - Image processing library

---

## ▶️ How to Run

Follow these simple steps:

1. **Open terminal or command prompt**
2. **Navigate to the project folder:**
   ```bash
   cd path/to/project-folder
   ```
3. **Run the script:**
   ```bash
   python split_slides.py
   ```

The script will automatically process all PDFs in the `input slides/` folder.

---

## 📊 Example Terminal Output

```
🚀 Slide conversion started

📄 Processing: lec 01 topic.pdf
  Page 1/8
    Slide 1
    Slide 2
    Slide 3
    Slide 4
  Page 2/8
    Slide 5
    Slide 6
    Slide 7
    Slide 8
  ...
  
  Saving 32 slides...
  ✅ Done
  📁 Saved as: lec 01 topic_slide_adjusted.pdf

📄 Processing: lec 02 ontology.pdf
  ...

🎉 All PDFs processed successfully!
```

---

## 📝 Output File Naming

The script automatically generates descriptive output filenames:

| Input File | Output File |
|------------|-------------|
| `lec 01 topic.pdf` | `lec 01 topic_slide_adjusted.pdf` |
| `lec 02 ontology.pdf` | `lec 02 ontology_slide_adjusted.pdf` |

Each page in the output PDF contains **exactly one slide**.

---

## ⚙️ Configuration (Optional)

You can customize the output quality by modifying this value in the script:

```python
DPI = 200  # Default: balanced quality and performance
```

**Recommended settings:**

| DPI Value | Quality | Memory Usage | Best For |
|-----------|---------|--------------|----------|
| `150` | Basic | Very Low | Weak PCs, quick previews |
| `200` | Good | Moderate | **Recommended default** |
| `300` | High | High | Printing, archival quality |

---

## ⚠️ Limitations

- Assumes **exactly 4 slides per page** in a **2×2 grid layout**
- Slides must be **evenly aligned** on the source page
- Layout detection is **not automatic** (kept simple by design for reliability)
- Works best with standard lecture slide formats

---

## 🎓 Intended Use Cases

Perfect for:

- 📚 University lecture notes and study materials
- 📝 Exam preparation and revision
- 🔬 Research papers and systematic literature reviews (SLR)
- 🖨️ Printing handout slides in a readable format
- 📖 Creating digital study guides

---

## 🤝 Contributing

Contributions and improvements are welcome! Areas for enhancement:

- 🚀 Performance optimizations
- 📐 Support for other slide layouts (3×3, 6 per page, etc.)
- 🎨 Automatic padding and centering improvements
- 🖥️ GUI implementation for non-technical users
- 🔧 Command-line argument support

Feel free to submit pull requests or open issues on GitHub!

---

## 📜 License

This project is released under the **MIT License**.

✅ Free to use  
✅ Free to modify  
✅ Free to distribute

---

## 💡 Tips

- **Batch processing:** Place all PDFs you want to convert in the `input slides/` folder
- **Check output:** Always verify the first converted PDF before processing large batches
- **Disk space:** Ensure you have enough space (output files are typically 2-3x the input size)
- **Backup:** Keep original PDFs in a separate location

---

## 🐛 Troubleshooting

**Issue:** "Module not found" error  
**Solution:** Run `pip install pymupdf pillow`

**Issue:** Output slides look blurry  
**Solution:** Increase the `DPI` value to `300`

**Issue:** Script runs out of memory  
**Solution:** Decrease the `DPI` value to `150` or process files one at a time

---

⭐ **If you find this project useful, please consider starring the repository on GitHub!**

---

**Made with ❤️ for students and educators**
