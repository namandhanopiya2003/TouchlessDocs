import fitz  
import cv2
import numpy as np

# Class to handle PDF viewing
class PDFViewer:
    def __init__(self, path):
        # Opens the PDF document
        self.doc = fitz.open(path)
        # Starts at the first page
        self.page_number = 0

    # Renders the current page as an image (to display with OpenCV)
    def render_page(self):
        page = self.doc[self.page_number]
        pix = page.get_pixmap()
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
        # Converts RGB to BGR for OpenCV
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Moves to the next page
    def next_page(self):
        if self.page_number < len(self.doc) - 1:
            self.page_number += 1

    # Moves to the previous page
    def prev_page(self):
        if self.page_number > 0:
            self.page_number -= 1

