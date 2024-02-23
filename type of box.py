import fitz
import numpy as np

def calculate_eccentricity(width, height):
    a = max(width, height) / 2
    b = min(width, height) / 2
    return np.sqrt(1 - (b**2 / a**2))

def identify_box_type(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        if page_num>4:
            page = doc[page_num]
            blocks = page.get_text("blocks")
            for block in blocks:
                if not isinstance(block, (list, tuple)) or len(block) < 4:
                    continue

                x, y, width, height = block[:4]
                aspect_ratio = width / height
                rectangular_threshold = 1.5
                oval_threshold = 0.8
                if aspect_ratio >= rectangular_threshold:
                    box_type = 'Rectangular'
                elif aspect_ratio < oval_threshold:
                    box_type = 'Oval'
                else:
                    box_type = 'Unknown'
                if box_type==('Rectangular' or 'Oval'):
                    print(f"Box at ({x}, {y}) - Type: {box_type}")
                    text_content=block[4]
                    print(text_content)
            # Additional print statements to inspect the structure of 'block'
            #print("Block:", block)
            #print("Type of block[0]:", type(block[0]))

    doc.close()

identify_box_type(r"C:\Users\anusha.raparthi\Downloads\TLS - EMCTTW_Phase I_Workflow - V4.pdf")

