import cv2

def draw_annotation(frame, points):
    for pt in points:
        cv2.circle(frame, pt, 5, (0, 255, 0), -1)
    return frame
