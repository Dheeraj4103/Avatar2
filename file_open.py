import os
from engine1 import speak


def File(query):
    f = query[5:]
    c_dir = r"C:\\"
    d_dir = r"D:\\"
    e_dir = r"E:\\"
    itemc = os.listdir(c_dir)
    itemd = os.listdir(d_dir)
    iteme = os.listdir(e_dir)

    for i in range(0, len(itemc)):
        if itemc[i].lower() == f:
            speak("Opening...")
            os.startfile(os.path.join(c_dir, itemc[i]))
            break

    for m in range(0, len(itemd)):
        if itemd[m].lower() == f:
            speak("Opening...")
            os.startfile(os.path.join(d_dir, itemd[m]))
            break

    for n in range(0, len(iteme)):
        if iteme[n].lower() == f:
            speak("Opening...")
            os.startfile(os.path.join(e_dir, iteme[n]))
            break
        elif n == (len(iteme) - 1):
            if iteme[n].lower() == f:
                speak("Opening...")
                os.startfile(os.path.join(e_dir, iteme[n]))
                break

    # if (f not in itemc) and (f not in itemd) and (f not in iteme):
    #     speak("File not found")
