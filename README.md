# 📄 PDF Slide Splitter (4 Slides → 1 Slide per Page)

A simple Python tool to convert **lecture PDFs with 4 slides per page** into a **clean PDF where each page contains exactly one slide**.

Ideal for students, researchers, and lecturers who receive handout-style slides and want a more readable format.

---

## ✨ Features

- Converts **4 slides per page → 1 slide per page**
- Batch processes **multiple PDF files**
- Shows **progress in the terminal**
- Safe for **low-performance PCs**
- Beginner-friendly and easy to modify
- Clean and readable output PDFs

---

## 📁 Folder Structure

Create the following structure before running the script:

project-folder/
├── input slides/
│ ├── lec 01 topic.pdf
│ ├── lec 02 ontology.pdf
├── output slides/
│ └── (converted PDFs will appear here)
└── split_slides.py


- Place original PDFs inside **input slides/**
- Converted PDFs will be saved inside **output slides/**

---

## 🛠 Requirements

### Python
- Python **3.8 or higher**

Check your Python version:

python --version


### Required Libraries
Install required packages using pip:

pip install pymupdf pillow

---

## ▶ How to Run

1. Open a terminal or command prompt
2. Navigate to the project folder
3. Run the script:

python split_slides.py


---

## 📊 Example Terminal Output

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
...

Saving 32 slides...
✅ Done
📁 Saved as: lec 01 topic_slide_adjusted.pdf

🎉 All PDFs processed successfully!


---

## 📝 Output File Naming

**Input file:**

lec 01 topic.pdf

**Output file:**

lec 01 topic_slide_adjusted.pdf


Each page in the output PDF contains **one slide**.

---

## ⚙ Configuration (Optional)

You can adjust output quality by changing this value in the script:

DPI = 200


- `150` → Very low memory usage
- `200` → Recommended (balanced quality and performance)
- `300` → High quality (may be heavy on weak PCs)

---

## ⚠ Limitations

- Assumes **exactly 4 slides per page (2×2 layout)**
- Slides must be evenly aligned
- Layout detection is not automatic (kept simple by design)

---

## 🎓 Intended Use

- University lecture notes
- Exam preparation
- Research and SLR documentation
- Printing handout slides neatly

---

## 🤝 Contributing

Contributions are welcome:
- Performance improvements
- Support for other slide layouts
- Padding and centering enhancements
- GUI implementation

---

## 📜 License

Released under the **MIT License**.  
Free to use, modify, and distribute.

---

⭐ If you find this project useful, consider starring the repository on GitHub!
