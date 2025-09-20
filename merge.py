import os
import PyPDF2
import argparse

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()

    for pdf in input_files:
        if not os.path.exists(pdf):
            print(f"File not found: {pdf}")
            continue
        merger.append(pdf)

    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one.")
    parser.add_argument("pdfs", nargs='+', help="PDF files to merge")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Output filename (default: merged.pdf)")
    args = parser.parse_args()

    merge_pdfs(args.pdfs, args.output)
