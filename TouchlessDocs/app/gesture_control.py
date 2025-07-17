import cv2
import mediapipe as mp
from utils.gesture_rules import is_pinch, is_swipe_left, is_five_fingers_open

mp_hands = mp.solutions.hands

class GestureController:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6)

    def detect_gestures(self, frame):
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            coords = [(lm.x, lm.y) for lm in landmarks]

            if is_pinch(coords):
                return "pinch"
            elif is_swipe_left(coords):
                return "swipe_left"
            elif is_five_fingers_open(coords):
                return "open_palm"
        return "none"
