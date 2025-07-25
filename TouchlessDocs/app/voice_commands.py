import speech_recognition as sr
from utils.nlp_utils import classify_intent

class VoiceCommandProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_classify(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return classify_intent(text)
            except sr.UnknownValueError:
                return None
