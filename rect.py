import fitz  # PyMuPDF
import cv2
import numpy as np
import pytesseract

def extract_text_from_rectangles(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        # Render the page as an image
        pix = page.get_pixmap()

        # Convert the image to a NumPy array
        img_np = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, 3))

        # Convert the image to grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through contours and identify rectangles
        for contour in contours:
            # Approximate the contour to a polygon
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # If the polygon has four vertices, it's likely a rectangle
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)

                # Crop the rectangle from the grayscale image
                roi = gray[y:y+h, x:x+w]

                # Use pytesseract to perform OCR on the cropped region
                text = pytesseract.image_to_string(roi)

                print(f"Identified rectangle on page {page_number + 1}: x={x}, y={y}, width={w}, height={h}")
                print(f"Text inside the rectangle: {text.strip()}\n")

    # Close the PDF file
    pdf_document.close()

# Replace 'your_pdf_path.pdf' with the path to your PDF file
extract_text_from_rectangles(r"C:\Users\anusha.raparthi\Downloads\TLS - Gland - Change Control -PFD.pdf")
