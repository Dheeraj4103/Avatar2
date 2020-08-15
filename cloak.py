import datetime


def time():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    return strtime


def date():
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    return date
