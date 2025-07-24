import math

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def is_pinch(hand_landmarks):
    thumb_tip = hand_landmarks[4]
    index_tip = hand_landmarks[8]
    return distance(thumb_tip, index_tip) < 0.04  

def is_swipe_left(hand_landmarks):
    wrist = hand_landmarks[0]
    index_tip = hand_landmarks[8]
    return index_tip[0] < wrist[0] - 0.2 

def is_five_fingers_open(hand_landmarks):
    fingers = [8, 12, 16, 20]
    return all(hand_landmarks[f][1] < hand_landmarks[f-2][1] for f in fingers)
