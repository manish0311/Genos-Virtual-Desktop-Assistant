import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good Morning Sir!")

    elif hour >= 12 and hour <= 17:
        speak(" Good Afternoon Sir!")

    else:
        speak(" Good Evening Sir!")

    speak("I am Genos. Please tell me how may I help you!")


def takeCommand():
    # It takes microphone input from the user and returns string output

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
        print("Oops! Sorry the given command is not recognized by the system! Please try again...")
        speak("Oops! Sorry the given command is not recognized by the system! Please try again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
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
            sys.exit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            sys.exit()

        elif 'open google' in query:
            webbrowser.open("google.com")
            sys.exit()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            sys.exit()

        elif 'play batman arkham city' in query:
            arkham_city = 'E:\\Installation\\Batman - Arkham City\\Launcher'
            os.startfile(arkham_city)
            sys.exit()

        elif 'play batman arkham asylum' in query:
            arkham_asylum = 'E:\\Installation\\Batman Arkham Asylum - Game of the Year Edition\\Binaries\\BmLauncher'
            os.startfile(arkham_asylum)
            sys.exit()

        elif 'play dmc4' in query:
            dmc4 = 'C:\\R.G. Catalyst\\Devil May Cry 4\\DMC4Launcher'
            os.startfile(dmc4)
            sys.exit()

        elif 'play hitman' in query:
            hitman = 'E:\\Installation\\Hitman Absolution\\HMA'
            os.startfile(hitman)
            sys.exit()

        elif 'open the anime folder' in query:
            anime = 'D:\\Anime'
            os.startfile(anime)
            sys.exit()

        elif 'open the cartoons folder' in query:
            animated = 'E:\\Movies\\Animated'
            os.startfile(animated)
            sys.exit()

        elif 'open the hollywood folder' in query:
            hollywood = 'E:\\Movies\\Hollywood'
            os.startfile(hollywood)
            sys.exit()

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            play = random.choice(songs)
            os.startfile(os.path.join(music_dir, play))
            sys.exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            sys.exit()

        elif 'open code' in query:
            codePath = "E:\\Installation\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            sys.exit()

        elif 'open pycharm' in query:
            pyCharm = "E:\\Installation\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64"
            os.startfile(pyCharm)
            sys.exit()

        elif 'open atom' in query:
            atomPath = "C:\\Users\\Home\\AppData\\Local\\atom\\atom"
            os.startfile(atomPath)
            sys.exit()
