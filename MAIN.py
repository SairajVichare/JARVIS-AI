import subprocess
import winshell
import pyttsx3 #pip install pyttsx3
import pywhatkit
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import wolframalpha
from urllib.request import urlopen
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sairajvichare876@gmail.com', 'wjyzwcscdnvwlivk')
    server.sendmail('ashupatil2144@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open Amazon' in query:
            webbrowser.open("amazon.in")


        elif 'play ' in query:
            song=query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is"+strTime)

        elif 'tell me joke ' in query:
            speak(pyjokes.get_joke())

        elif ' are you single' in query:
            speak("i am in relationship with wifi")


        elif 'date ' in query:

            strDate = datetime.datetime.now().strftime("%B:%D:%Y")
            print(strDate)
            speak("Sir, the date is" + strDate)

        elif 'email to sairaj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sairajvichare876@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sairaj. I am not able to send this email")

        elif 'how are you' in query:
            speak("i am fine sir, thank you")
            speak("how are you sir")

        elif 'fine' in query:
            speak("its good to know that your fine")


        elif 'who made you' in query:
            speak("i have been created by Tony Stark")


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
            speak("Recycle Bin Recycled")

        elif 'exit' in query:
            speak("thanks for giving me your time sir")
            exit()

        elif 'restart system' in query:
            subprocess.call(["shutdown","/r"])

        elif 'shutdown system' in query:
            speak("hold on a sec! your system is on its way to shut down")
            subprocess.call('shutdown/p/f')


