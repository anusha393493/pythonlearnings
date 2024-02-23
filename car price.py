import fitz  # PyMuPDF
import cv2
import numpy as np

def identify_rectangles_in_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

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
                print(f"Identified rectangle on page {page_number + 1}: x={x}, y={y}, width={w}, height={h}")

    # Close the PDF file
    pdf_document.close()

# Replace 'your_pdf_path.pdf' with the path to your PDF file
identify_rectangles_in_pdf(r"C:\Users\anusha.raparthi\Downloads\TLS - Gland - Change Control -PFD.pdf")


