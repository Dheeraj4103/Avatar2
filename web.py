import webbrowser as w
import wikipedia
from engine1 import speak
import os


path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def search(query):

    if "who is" in query:
        qr = query[7:]
        result = wikipedia.summary(qr, sentences=2)
        speak(result)

    elif "what is" in query:
        qry = query[8:]
        w.get(path).open(f"https://www.google.com/search?q={qry}")

    elif "tell me about" in query:
        qry = query[14:]
        w.get(path).open(f"https://www.google.com/search?q={qry}")

    elif "show me about" in query:
        qry = query[14:]
        w.get(path).open(f"https://www.google.com/search?q={qry}")

    # Youtube search
    elif "search" and "on youtube" in query:
        qre = query[7:-11]
        qrel = qre.split()
        qre2 = '+'.join(qrel)

        w.get(path).open(
            f"https://www.youtube.com/results?search_query={qre2}")


def start(query):
    if "google" in query:
        speak("Opening...")
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
        os.startfile(path)

    # open youtube
    elif "youtube" in query:
        speak("Opening...")
        path1 = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        w.get(path1).open("https://www.youtube.com/?gl=IN")


def none(query):
    w.get(path).open(f"https://www.google.com/search?q={query}")
