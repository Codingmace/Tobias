import os
import sys
import datetime
import math

def sleep():
    print("Going to sleep")
    sys.exit()

def shutdown(platform):
    print("Shutting down")
    if platform == "win32":
        os.system("shutdown /p /f")
    if platform == "linux" or "darwin" or "linux2":
        os.system("poweroff")


def screenshot(folderPath):
    import pyautogui
    img = pyautogui.screenshot()
    dirExist(folderPath)
    dateTime = (datetime.datetime.now().replace(microsecond=0).strftime('%H-%M-%S'))
    img.save(folderPath + '/screenshot ' + (dateTime)+ '.png')
    return "Taking Screenshot"

def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)



def getTime(military):
    if military:
        return datetime.datetime.now().strftime("%H:%M:%S")
    hour = datetime.datetime.hour
    hour = datetime.datetime.minute
    hour = datetime.datetime.second
    extend = "AM"
    if hour > 12:
        hour -= 12
        extend = "PM"
    return str(hour + ":" + minute + ":" + second+ " " + extend)

def changeVoice(curVoice):
    if voiceId == 1:
        return 0
    elif voiceId == 0:
        return 1
    

def searchWiki(query):
    import wikipedia
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    return results

## Need to do more to this
def diagnostics():
    import psutil
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    
    return str("CPU is at " + usage + " and batter is at " + str(battery.percent))

def playMyMusic(path):
    os.startfile(path) # If file doesn't exist throw an error or something

def calculate(query):
    # Basic one words responses
    split= query.split(" ", "")
    if "pi" in query:
        return float(math.pi)
    elif "tan" in query:
        return float(math.tan(float(split[1])))
    elif "sin" in query:
        return float(math.sin(float(split[1])))
    elif "cos" in query:
        return float(math.cos(float(split[1])))
    elif "factorial" in query:
        query = query.replace("factorial of ","")
        query = query.replace("factorial","")
        return float(math.factorial(float(query)))
    elif "value of e" in query:
        return float(math.e)
    elif "add" in query:
        return float(split[1]) + float(split[3])
    elif "subtract" in query:
        return float(split[1]) - float(split[3])
    elif "multiply" in query:
        return float(split[1]) * float(split[3])
    elif "divide" in query:
        return float(split[1]) / float(split[3])
    elif "plus" in query:
        return float(split[0]) + float(split[2])
    elif "minus" in query:
        return float(split[0]) - float(split[2])
    elif "times" in query:
        return float(split[0]) * float(split[2])
    elif "divided by" in query:
        return float(split[0]) / float(split[3])
    elif "to the" in query:
        return float(split[0]) ** float(split[5])
    elif "log" in query:
        if "base" in query:
            return float(math.log(float(split[1]), float(split[3])))
        else:
            return float(math.log(float(split[1]), 10))
    else :
        return -1

    # No where near done
def advanceCalculations(query):
    # Advance Equations
    words = ["plus"]
    symbols = ["+"]
    split = query.split(" ")
    equasion = ""
    for s in split:
        if s in words:
            equation += symbols[words[s]]
        else:
            equation += s
    print(equasion)
    # Alternative way
    i = 0
    for w in words:
        query = query.replace(w, symbol[i])
        i += 1
    print(query)
    
    return "Done"



