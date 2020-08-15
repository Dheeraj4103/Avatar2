import datetime
import pyttsx3
import file_open
import cloak
import web
import random
import os
from engine2 import speak
import speech_recognition as sr
from user_cred1 import SignUp


def Greetings():

    time = int(datetime.datetime.now().hour)
    if time >= 12 and time < 16:
        speak("Good Afternoon Sir")
    elif time >= 0 and time < 12:
        speak("Good Morning Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Avatar, always at your service.")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def main():
    search_q = ['who is', 'what is', 'tell me about', 'show me about']
    bye_q = ['goodbye', 'turn off', 'shutdown', 'packup', 'bye', 'close']
    while True:
        query = input("Enter Command:- ").lower()
        # query = takecommand().lower()
        if "google" in query:
            web.start(query)

        elif "time" in query:
            speak(cloak.time())

        elif "date" in query:
            speak(cloak.date())
        elif 'search' in query:
            web.search(query)

        elif "youtube" in query:
            web.start(query)

        elif 'open' in query:

            file_open.File(query)

        elif 'how are you' in query:
            speak("Fine")

        elif 'note' in query:
            qry = " "+' ' + '\n' + f'{cloak.date()}  ' + \
                f'{cloak.time()}' + '\n' + query[5:] + '\n'
            with open("note.txt", 'a') as file:
                file.writelines(qry)
            speak("Ok Boss")

        elif 'nickname' in query:
            with open('nickname.txt', mode='r') as nick_file:
                name = nick_file.read()
            speak(f"My nickname is {name}")

        elif query in bye_q:
            speak("Good bye sir, see you soon")
            quit()
        else:
            for item in search_q:
                if item in query:
                    speak("Searching...")
                    web.search(query)

            for item in ['hi', 'hello']:
                if item in query:
                    speak("Hello sir, How can I help you")


a = SignUp()

if a == True:

    Greetings()
    main()


elif a == False:
    speak("Unauthenticated User")
elif a == "Exit":
    exit()
