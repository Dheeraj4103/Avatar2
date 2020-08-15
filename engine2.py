import os
from gtts import gTTS
from playsound import playsound
from google_trans import Translator, LANGCODES
import random
translator = Translator()


def speak(audio, lg='en'):

    translat = translator.translate(audio, dest=lg).text
    tts = gTTS(text=translat, lang=lg, slow=False)
    r = random.randint(1, 100000)
    file1 = 'audio_' + str(r) + '.mp3'
    tts.save(file1)
    playsound(file1)
    print(audio)
    os.remove(file1)


if __name__ == "__main__":
    speak("what are you doing vidhisha")
