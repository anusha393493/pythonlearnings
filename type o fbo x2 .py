import fitz
import numpy as np

def calculate_eccentricity(width, height):
    a = max(width, height) / 2
    b = min(width, height) / 2
    return np.sqrt(1 - (b**2 / a**2))

def identify_box_type(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        if page_num >4:
            page = doc[page_num]
            blocks = page.get_text("blocks")
            for block in blocks:
                if not isinstance(block, (list, tuple)) or len(block) < 4:
                    continue

                x, y, width, height = block[:4]
                aspect_ratio = width / height
                rectangular_threshold = 1.5
                round_rectangular_threshold = 0.8
                corner_keyword = "rounded"
                text_content = block[4]

                if aspect_ratio >= rectangular_threshold and corner_keyword in text_content.lower():
                    box_type = 'Round-Rectangular'
                elif aspect_ratio >= rectangular_threshold:
                    box_type = 'Rectangular'
                else:
                    box_type = 'Unknown'

                if box_type in ('Round-Rectangular', 'Rectangular'):
                    print(f"Page {page_num + 1}: Box at ({x}, {y}) - Type: {box_type}")
                    print("Text Content:", text_content)
                    print()

    doc.close()

identify_box_type(r"C:\Users\anusha.raparthi\Downloads\TLS - EMCTTW_Phase I_Workflow - V4.pdf")
