import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir. How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if  __name__ == "__main__":
    wishMe()
    while True:
        print("Listening...")
        query = takeCommand()

        #Logic for executing tasks base on query
        sites = [["youtube","https://youtube.com"],
                 ["spotify","https://spotify.com"],
                 ["wikipedia","https://wikipedia.com"],
                 ["google","https://google.com"]]
        
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])

        '''
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            '''

        if "open music" in query:
            os.startfile("C:/Users/SAYAK/Downloads/Aayi-Nai.mp3")
        
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time now is {strfTime}")

        if "stop now" in query:
            speak("Ok sir stopping now, have a nice day")
            break
