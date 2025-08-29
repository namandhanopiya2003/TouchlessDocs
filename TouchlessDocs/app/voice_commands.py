import speech_recognition as sr
from utils.nlp_utils import classify_intent

# Class to handle voice commands
class VoiceCommandProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    # Listen to the user's voice and figure out the command
    def listen_and_classify(self):
        # Use the microphone as input
        with sr.Microphone() as source:
            print("Listening...")
            # To record audio
            audio = self.recognizer.listen(source)
            try:
                # Converts speech to text using Google API
                text = self.recognizer.recognize_google(audio)
                # Classify the text into an intent (like next_page or prev_page)
                return classify_intent(text)
            except sr.UnknownValueError:
                # Return None if speech couldn't be understood
                return None
