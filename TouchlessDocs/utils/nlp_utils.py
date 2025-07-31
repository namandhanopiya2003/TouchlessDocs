import re

COMMANDS = {
    "next_page": ["next", "forward", "go ahead"],
    "prev_page": ["back", "previous", "go back"],
    "zoom_in": ["zoom in", "bigger"],
    "zoom_out": ["zoom out", "smaller"],
    "save": ["save", "store", "record"]
}

def classify_intent(text):
    text = text.lower()
    for intent, phrases in COMMANDS.items():
        if any(re.search(rf"\b{phrase}\b", text) for phrase in phrases):
            return intent
    return "unknown"
