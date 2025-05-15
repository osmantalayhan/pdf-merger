# 🧾 PDF Merger

A minimal and professional Python CLI tool that merges multiple PDF files into a single file.

Perfect for automating your job applications, consolidating reports, or simplifying documentation.

---

## ✨ Features

- 🔹 Merge unlimited number of PDFs
- 🔹 Clean and simple command-line interface (CLI)
- 🔹 No GUI needed, works on any OS with Python
- 🔹 Lightweight and fast

---

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/pdf-merger.git
cd pdf-merger
pip install -r requirements.txt
```

# ⚙️ Usage
Run the tool from the command line:
```bash
python merge.py file1.pdf file2.pdf file3.pdf -o merged.pdf
```

# ✅ Example
```bash
python merge.py resume.pdf transcript.pdf certificate.pdf -o job-application.pdf
```
This command will merge the three files into one PDF called job-application.pdf.


# 🛠️ Arguments

| Argument              | Description                                |
|-----------------------|--------------------------------------------|
| `file1.pdf file2.pdf` | List of input PDF files to be merged       |
| `-o merged.pdf`       | (Optional) Name of the output file          |

> Default output file is `merged.pdf` if `-o` is not specified.

# 📦 Requirements

- Python 3.6+
- PyPDF2

Install with:
```bash
pip install PyPDF2
```

# 🙌 Contributing
Feel free to open a PR or issue. Let's build cool tools together!
Looking to practice GitHub collaboration? Open a pull request with a README improvement or code refactor ✨

This project was built as part of a GitHub skills showcase to demonstrate Python scripting, clean CLI design, and real-world utility.
Created with by @osmantalayhan
