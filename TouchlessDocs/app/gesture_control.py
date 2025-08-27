import cv2
import mediapipe as mp
from utils.gesture_rules import is_pinch, is_swipe_left, is_five_fingers_open

# Initializes MediaPipe Hands module
mp_hands = mp.solutions.hands

# Class to handle gesture detection using MediaPipe
class GestureController:
    def __init__(self):
        # Initializez the Hands model with detection and tracking confidence thresholds
        self.hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6)

    # Function to detect gestures from a video frame
    def detect_gestures(self, frame):

        # It converts frame from BGR to RGB and process with MediaPipe Hands
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # If at least one hand is detected
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            coords = [(lm.x, lm.y) for lm in landmarks]

            # Checks for specific gestures using predefined rules
            if is_pinch(coords):
                return "pinch"
            elif is_swipe_left(coords):
                return "swipe_left"
            elif is_five_fingers_open(coords):
                return "open_palm"
        return "none"
