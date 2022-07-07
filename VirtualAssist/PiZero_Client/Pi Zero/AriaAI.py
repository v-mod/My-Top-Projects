import speech_recognition as sr
from gtts import gTTS
import os
import requests
import random
import filePlayer
import pixelController
pixels = pixelController.Pixels()
def speak(text):
    tts = gTTS(text)
    tts.save('tts.mp3')
    filePlayer.play('tts.mp3')
def takeCommand():
    pixels.wakeup()
    pixels.listen()
    r=sr.Recognizer()
#    requests.get('localhost:5000/mic/on')
    filePlayer.play('on.mp3')
    with sr.Microphone() as source:
        audio=r.listen(source,phrase_time_limit=5)
        try:
            statement=r.recognize_google(audio,language='en-gb')
            print(f'<-t: {statement}\n')
#            requests.get('localhost:5000/mic/off')
            filePlayer.play('off.mp3')
        except Exception as e:
            filePlayer.play('off.mp3')
#            requests.get('localhost:5000/mic/off')
            speak("Pardon me, please say that again")
            return takeCommand()
        return statement
def check():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-gb')
        except Exception as e:
            return "None"
        return statement