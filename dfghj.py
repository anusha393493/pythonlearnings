import re
from pdfminer.high_level import extract_pages,extract_text
import PyPDF2
def count_backslash(text):
    n_count=text.count('\\n')
    return n_count




for page_data in extract_pages(r"C:\Users\anusha.raparthi\Downloads\TLS - EMCTTW_Phase I_Workflow - V4.pdf"):

    for t in page_data:
        text=str(t)
        print(text)
        match = re.search(r'\b(\d+\.\d+)', text)

        if match:
            extracted_value = match.group(1)
            print("Extracted value:", extracted_value)
        else:
            print("No match found.")

        result = count_backslash(text)
        print("Number of backslashes:",result)

#print(t)
'''
def text_pattern(text):
    for line in text:
        c=text.strip()
        c=str(c)
        a=re.compile(r".*[2,9].*\d{2,}|800.*\\n.*")
        match=a.match(c)
        if match:
            print("Match found:", match)
        else:
            print("No match")

extracted_text=text_pattern(text)
'''

