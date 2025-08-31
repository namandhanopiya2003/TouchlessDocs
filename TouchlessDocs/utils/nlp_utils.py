import re

# List of commands and words/phrases that mean the same thing
COMMANDS = {
    "next_page": ["next", "forward", "go ahead"],
    "prev_page": ["back", "previous", "go back"],
    "zoom_in": ["zoom in", "bigger"],
    "zoom_out": ["zoom out", "smaller"],
    "save": ["save", "store", "record"]
}

# Function to figure out the user's intention from text
def classify_intent(text):
    # Makes text lowercase for easier matching
    text = text.lower()
    for intent, phrases in COMMANDS.items():
        # Checks if any phrase for this intent is in the text
        if any(re.search(rf"\b{phrase}\b", text) for phrase in phrases):
            return intent                # Return the matching command
    return "unknown"                     # If no match, return 'unknown'
