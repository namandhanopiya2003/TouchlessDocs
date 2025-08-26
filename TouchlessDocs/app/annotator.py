import cv2

# Function to draw annotations (or dots) on a given frame
def draw_annotation(frame, points):

    # Loop through all points and draw a green circle for each
    for pt in points:
        cv2.circle(frame, pt, 5, (0, 255, 0), -1)

    # Returns the frame with the drawn annotations
    return frame
