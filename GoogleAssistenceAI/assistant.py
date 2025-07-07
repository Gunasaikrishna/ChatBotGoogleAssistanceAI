import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import json

# Load intent patterns
with open("intents.json") as file:
    intents = json.load(file)

# Text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice recognition setup
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def match_intent(user_input):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent["tag"], intent["responses"]
    return "unknown", ["Sorry, I didn’t understand that."]

def handle_action(tag):
    if tag == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")
    elif tag == "open_google":
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif tag == "open_facebook":
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
    elif tag == "open_youtube":
        speak("Opening Youtube.")
        webbrowser.open("https://www.youtube.com")
        
    elif tag == "exit":
        speak("Goodbye!")
        exit()

# Start assistant
speak("Hello! I'm your voice assistant. Just talk to me.")
while True:
    command = listen()
    if command:
        tag, responses = match_intent(command)
        speak(responses[0])
        handle_action(tag)
