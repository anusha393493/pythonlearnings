import re
from pdfminer.high_level import extract_pages, extract_text
import PyPDF2

def count_backslash(text):
    n_count = text.count('\\n')
    return n_count

pdf_path = r"C:\Users\anusha.raparthi\Downloads\TLS - Gland - Change Control -PFD.pdf"

for page_number, page_data in enumerate(extract_pages(pdf_path), start=1):
    for t in page_data:
        text = str(t)
        match = re.search(r'\b(\d+\.\d+)', text)
        result = count_backslash(text)
        if match:
            extracted_value = match.group(1)
        else:
            print("No match found.")
        if float(extracted_value) > 250 and float(extracted_value) < 300 and int(result) == 1 and page_number>5:
            print("Page:", page_number)
            print(text)
            print("Extracted value:", extracted_value)
            print("Number of backslashes:", result)











