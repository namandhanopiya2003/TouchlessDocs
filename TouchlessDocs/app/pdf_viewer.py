import fitz  
import cv2
import numpy as np

class PDFViewer:
    def __init__(self, path):
        self.doc = fitz.open(path)
        self.page_number = 0

    def render_page(self):
        page = self.doc[self.page_number]
        pix = page.get_pixmap()
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    def next_page(self):
        if self.page_number < len(self.doc) - 1:
            self.page_number += 1

    def prev_page(self):
        if self.page_number > 0:
            self.page_number -= 1
