#!/usr/bin/python3

import os
import sys
import configparser

def intro():
    print("Hello and welcome to the setup of Tobias")
    print("This program is a little big if you download everything")
    print("I made it better by only downloading what you need")
    print("Well let us begin")

def keys():
    allready = os.path.exists("API\variables.py")
    if allready:
        print("That already exists")
        allready = input("Do you want to override it? (yes/no) ").strip() == "yes"

    if allready:
        return

    rapidValid = False
    rapidApiSelect = input("Do you have a rapidAPIKey (yes/no)? ").strip().lower()
    rapidApi = "3f9620697cmsh4d8a1a910032d97p15547bjsn7f4d1d89819c"
    if rapidApiSelect == "yes" or rapidApiSelect == "y":
        while not rapidValid:
            rapidApi = input("Please input your rapidApiKey now: ").strip()
            if len(rapidApi) == 50:
                print("The length is 50 so most likely a valid key")
                rapidValid = True
            else:
                print("That doesn't seem to be the right. Length of " + len(rapidApi))
                temp = input("Is " +rapidApi + " correct (yes/no)?")
                rapidValid = "yes" in temp.lower()

    else:
        print("That sucks. Using Default Key and Limiting the API able to use")

    dncValid = False
    dncValidSelect = input("Do you have a doNotCall ApiKey (yes/no)? ").strip().lower()
    dncApi = ""
    if dncValidSelect == "yes" or dncValidSelect == "y":
        while not dncValid:
            dncApi = input("Please input your doNotCallApiKey now: ").strip()
            if len(dncApi) == 40:
                print("The length is 40 so most likely a valid key")
                dncValid = True
            else:
                print("That doesn't seem to be the right. Length of "+ len(dncApi))
                temp = input("Is " + dncApi + " correct (yes/no)?")
                dncValid = "yes" in temp.lower()
    else:
        print("Oh boy. Disabling the DoNotCall Database")

    print("Writting information to file variables.py")
    print("You can change the information later on if you would like")
    f = open("API/variables.py", "w")
    
    variableInfo = "rapidApiKey = \"" + rapidApi + "\"\ndncApiKey = \"" + dncApi + "\"\n"
    variableInfo2 = 'weatherInfo = {"language" : "english", "lang" : "en", "units": "e", "callback": "test", "mode":"JSON", "types": "link, accurate", "measurement":"imperial", "count": "10"} # Can change measurement to metric\n'
    f.write(variableInfo)
    f.write(variableInfo2)
    enableSpeech = input("Would you like to enable speech? ").strip().lower()
    if enableSpeech == "yes" or enableSpeech == "y":
        f.write("speechEnabled = True\n")
    else:
        f.write("speechEnabled = False\n")
    faceRecog = input("Would you like to enable Facial Recognition? ").strip().lower()
    if faceRecog == "yes" or faceRecog == "y":
        f.write("faceEnabled = True\n")
    else:
        f.write("faceEnabled = False\n")
    f.flush()
    f.close()

def printLogo():
    f = open("AsciiLogo.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line.strip())
    f.close()

def createRequirements():
    print("Here we select what we want to add to the requirements. Some people don't want to dowload everything")
    print("Later on that may become a huge file and nobody wants to waste space")
    print("Options:\n1.All\n2.Minimal\n3.Basic\n4.Speech\n5.Google")
    selection = int(input("Input your selection: "))
    allReqs = configparser.ConfigParser()
    allReqs.read("Data/allRequirements.ini")
    req = open("requirements.txt", "w")
    downloading = []
    if selection == 1: # Just copy the file
        for section in allReqs:
            for line in allReqs[section]:
                req.write(line + "==" + allReqs[section][line].strip('\"') + "\n")
    if selection >= 2 and selection <= 5: # Incrementally figure it out
        downloading.append("minimal")
        if selection >= 3:
            downloading.append("basic")
            if selection == 4:
                downloading.append("speech")
                if sys.platform == "win32":
                    downloading.append("speech-win32")
            if selection == 5:
                downloading.append("google")
        for section in downloading:
            for line in allReqs[section]:
                try:
                    req.write(line + "==" + allReqs[section][line].strip('\"') + "\n")
                except:
                    print("There was an issue. Flushing the file and closing it.")
                    req.flush()
                    req.close()
                    return
    req.flush()
    req.close()
    print("Ok we have written the requirements file. Now just run 'pip install -r requirements.txt'")

def main():
    intro()
    keys()
    printLogo()
    createRequirements()

main()
