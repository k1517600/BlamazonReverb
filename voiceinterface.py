import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os

project_id = "alrighty-alex"


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return listen()


def speak(text: str):
    audio = gTTS(text, lang='en', tld='co.uk')
    if os.path.isfile("response.mp3"):
        os.remove("response.mp3")

    audio.save("response.mp3")
    playsound("response.mp3")
