import cv2
from app.gesture_control import GestureController
from app.pdf_viewer import PDFViewer
from app.voice_commands import VoiceCommandProcessor
from app.session_logger import log_interaction

def run_app():

    # Initialize webcam
    cam = cv2.VideoCapture(0)
    # Initialize gesture controller
    gesture_ctrl = GestureController()
    # Initialize voice command processor
    voice_ctrl = VoiceCommandProcessor()
    # Initialize PDF viewer with example PDF
    viewer = PDFViewer("assets/example.pdf")

    # Main application loop
    while True:
        # Captures frame from webcam
        ret, frame = cam.read()
        if not ret:
            break

        # Detects gesture in the current frame
        gesture = gesture_ctrl.detect_gestures(frame)
        if gesture == "pinch":
            viewer.next_page()                                                 # Moves to next page
            log_interaction("gesture", {"type": "pinch -> next_page"})
        elif gesture == "swipe_left":
            viewer.prev_page()                                                 # Move to previous page
            log_interaction("gesture", {"type": "swipe_left -> prev_page"})

        # Renders current page of PDF
        doc_frame = viewer.render_page()
        # Displays frame in a window
        cv2.imshow("TouchlessDocs", doc_frame)

        key = cv2.waitKey(1)
        # Voice command mode
        if key == ord("v"):
            intent = voice_ctrl.listen_and_classify()
            log_interaction("voice", {"intent": intent})
            if intent == "next_page":
                viewer.next_page()
            elif intent == "prev_page":
                viewer.prev_page()
        # To quit application
        elif key == ord("q"):
            break

    # Releases resources when done
    cam.release()
    cv2.destroyAllWindows()
