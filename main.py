import speech_recognition as sr
import webbrowser
import time
from time import ctime
import os
import playsound
from gtts import gTTS
import random

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            jarvis(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
            
        except sr.UnknownValueError:
            jarvis("sorry didn't get that")
        except sr.RequestError:
            jarvis("sorry voice service down")
        return voice_data 
def jarvis(audio_string): 
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+ str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        jarvis('My name is jarvis')
    if 'time' in voice_data:
        jarvis(ctime())
    if 'search' in voice_data:
        search=record_audio('what to do you want search for?')
        url='http://google.com/search?q='+search
        webbrowser.get().open(url)
        jarvis('Here is what i found about'+search)
    if 'find location' in voice_data:
        location=record_audio('which location you are searching for ')
        url='http://google.nl/maps/place/'+ location + '/&amp'
        webbrowser.get().open(url)
        jarvis('Here is the location of')
    if 'exit' in voice_data:
        jarvis('ok,terminating')
        exit()         


                
time.sleep(1)
jarvis('How can I help You?')
while 1:
    voice_data=record_audio()
    respond(voice_data)


