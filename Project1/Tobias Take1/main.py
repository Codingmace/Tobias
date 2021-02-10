import webbrowser
import datetime
import os
import sys
import smtplib
import platform
import getpass

speechEnabled = False # Speech recognition/ Sating information enabed?
faceEnabled = False # Facial Recognition Feature Enabled?
def enableSpeechRecognition():
    import pyttsx3
    import speech_recognition as sr  #Implement later Automatic-speech recognition

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


def speak(text):
    if (speechEnabled):
        engine.say(text)
        engine.runAndWait()
    else:
        print(text)


# HERE DO ALL THE FACIAL RECOGNITION STUFF

# Do all diagnostics here


def takeCommand(query):
    return query

def greetings(machineName, userName):
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    speak(response)
    speak('I am ' + machineName + '. Please tell me how can I help you ' + userName + '?')


def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)
        return False
    return True


if __name__ == '__main__':
    if(speechEnabled):
        enableSpeechRecognition()
    from API.IPAddress import getMyIPv4Address, getMyIPv6Address
    print("Loading Config")
    machineName = "TOBIAS"
    machineMean = "Totally Obscure Intelligent Assistant System"
    platform = sys.platform
    name = "Master"
    noUsers = dirExist("User")
    userPath = "User/" + name + "/"
    userExists = dirExist(userPath)
    if not userExists:
        print("Have to create a user now")
    militaryTime = True
    voiceId = 1 # Female
    musicPath = userPath + "music/" # Later verify how much we start with
    browser= 'chrome' # Have this in all of them so can remove it
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))
    
    ipv4 = getMyIPv4Address()
    ipv6 = ""
    try:
        ipv6 = getMyIPv6Address()
    except:
        print("You do not have an IPv6 Address")

    cont = True
    from basicHelper import *
    from API.apiHandler import *
    from API.IPAddress import getMyIPv4Address, getMyIPv6Address
#    for q in queries:
    while cont:
        query = "are you there"
#        query = q
        cont = not cont

#        """ BASIC HELPER SECTION """
        if 'sleep' in query:
            speak("Going to sleep " +name)
            sleep()

        elif 'shutdown' in query:
            speak("Shutting down")
            shutdown(platform)

        elif 'your name' in query:
            speak("My name is "+ machineName)
            if 'stand for' in query:
                speak("which stands for " + machineMean)

        elif 'screenshot' in query:
            status = screenshot(userPath + "screenshot")
            speak(status)

        elif 'are you there' in query:
            speak(str("Yes " + name + ", " + machineName+ " at your service"))

        elif 'what time is it' in query:
            speak("The time is ")
            speak(getTime(militaryTime))

        elif 'change voice' in query:
            voiceId = changeVoice(voiceId)
            speak(str("Voice changed to " +("female" if voiceId == 0 else "male")))

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            results = searchWiki(query)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'diagnostics' in query:
            speak('Running Diagnostics')
            speak(diagnostics())

        elif 'get my ip' in query:
            if 'v4' in query:
                print(getMyIPv4Address())
                speak("I have gotten your IPv4 Address")
            elif 'v6' in query:
                try:
                    print(getMyIPv6Address())
                    speak("I have gotten your IPv6 Address")
                except:
                    speak("It seems you do not have an IPv6 Address")
                    speak("Now getting your IPv4 address")
                    print(getMyIPv4Address())
                    speak("I have gotten your IPv4 Address")
        elif 'get both my ip' in query:
            print(getMyIPv4Address())
            speak("I have gotten your IPv4 Address")
            try:
                print(getMyIPv6Address())
                speak("I have gotten your IPv6 Address")
            except:
                speak("It seems you do not have an IPv6 Address")

        elif 'play my music' in query:
            playMyMusic(musicPath)
            speak("Playing music")

        elif 'basic calculation' in query:
            query=query.replace("basic calculation", "")
            calculation = calculate(query)
            speak(query + " is equal to " + calculation)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(browser).open_new_tab("https://google.com")

#        """ API HELPER SECTION """
        elif 'define' in query: # Done
            word = query.replace('define', '')
            speak("The word " + word + "means " + wordDefinition(word))
            speak("Hope that definition works for you") # Could add returning an example

        elif 'google' in query:
            newQuery = query.replace("google", "")
            if "search" in query or "image" in query or "crawl" in query or "news" in query:
                result = google(newQuery)

        elif 'reverse image search' in query:
            newQuery = query.replace("reverse image search", "")
            print(reverseImageSearch(newQuery))

        elif 'proxy' in query:
            proxies = proxyCheck()
            dateTime = (datetime.datetime.now().replace(microsecond=0).strftime('%H-%M-%S'))
            tempFile = open(userPath + "op_" + dateTime + ".txt", "w")
            tempFile.write(proxies)
            tempFile.flush()
            tempFile.close()
            print(proxies[0]) # Check this works. Wasn't able to test today
            speak("I have returned the first openProxy and written the rest to a file")


        elif 'cat fact' in query:
            query = query.replace("cat fact","")
            speak(randomCatFact(query))

        elif 'weather' in query:
            query = query.replace("weather","")
            speak(weather(query))

        elif 'verify' in query:
            query = query.replace("verify", "").strip()
            speak(verifyPhoneNumber(query))
            
        elif "valid" in query: 
            query = query.replace("valid","").strip()
            speak(validateEmailAddress(query))
            
        elif 'analyze' in query:
            query = query.replace("analyze","")
            if 'text' in query:
                if "url" in query:
                    if "summarize" in query:
                        query = query.replace("text url summarize" ,"")
                        print(summarizeUrlText(query))
                        speak("I have printed out the text summary")
                    elif "extract" in query:
                        query = query.replace("text url extract","")
                        print(analyzeUrlText(query))
                        speak("I have printed out the text at the URL")
                    elif "grab" in query:
                        query = query.replace("text url grab","")
                        print(analyzeText(query))
                        speak("I have gotten the text at the URL")
                else:
                    speak("I do not think that is an option")
                    
            elif 'video' in query or 'image' in query:
                speak("This one doesn't work at all yet")
#                print(estimatePose(query)) 


        elif 'transcribe' in query:
            if 'audio to text' in query:
                query = query.replace("trascribe audio to text", "")
                speak ("I have not done the scripting for Transcribe.")
                speak("Please check back later")
#                print("Do the scripting for Transcribe")

        elif 'scan' in query:
            if 'url threat' in query:
                query = query.replace("scan url threat", "")
                print(detectUrlThreats(query))
                speak("Scanning the URL complete.") # Print result. If to file or console
            elif 'url link' in query:
                query = query.replace("scan url link", "")
                print(IntelligentUrl(query))
                speak("Scanning the URL complete.") # Print result. If to file or console
                
        elif 'image to text' in query:
            query = query.replace("image to text", "")
            imageText = urlImage2Text(query)
            speak("The image says:\n" + imageText) # Make adjustments to reason if it is a valid statement or not

        elif 'youtube' in query:
            if 'search' in query:
                speak("I don't think I have this one yet")
                speak("Alternatively I could open youtube.com and you look it up yourself")
                
            elif 'download' in query:
                query = query.replace("youtube download","")
                speak("Downloading Youtube File")
                status = downloadYoutube(query)
                speak("The download " + status)
            
        elif 'ip address' in query:
            if "to location" in query:
                speak(ip2Location(ipv4))
            if "geolocate" in query:
                speak(ipGeoLocate(ipv4))
            elif "world wide" in query:
                speak(ipLocWW(ipv4))

        elif 'plate scan' in query:
            query = query.replace("plate scan","")
            speak("Printing out plate information")
            print(plateRecognition(query))


#       """ Personal API Helper """
        


        

        elif 'more commands' in query:
            print("Print out the file with more commands")
            print("Made some more commands here")


        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")
