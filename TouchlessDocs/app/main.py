import cv2
from app.gesture_control import GestureController
from app.pdf_viewer import PDFViewer
from app.voice_commands import VoiceCommandProcessor
from app.session_logger import log_interaction

def run_app():
    cam = cv2.VideoCapture(0)
    gesture_ctrl = GestureController()
    voice_ctrl = VoiceCommandProcessor()
    viewer = PDFViewer("assets/example.pdf")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gesture = gesture_ctrl.detect_gestures(frame)
        if gesture == "pinch":
            viewer.next_page()
            log_interaction("gesture", {"type": "pinch -> next_page"})
        elif gesture == "swipe_left":
            viewer.prev_page()
            log_interaction("gesture", {"type": "swipe_left -> prev_page"})

        doc_frame = viewer.render_page()
        cv2.imshow("TouchlessDocs", doc_frame)

        key = cv2.waitKey(1)
        if key == ord("v"):
            intent = voice_ctrl.listen_and_classify()
            log_interaction("voice", {"intent": intent})
            if intent == "next_page":
                viewer.next_page()
            elif intent == "prev_page":
                viewer.prev_page()
        elif key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
