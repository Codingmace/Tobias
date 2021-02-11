import os

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
    rapidApiSelect = input("Do you have a rapidAPIKey (yes/no)? ")
    rapidApi = ""
    if "yes" in rapidApiSelect.lower():
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
        print("That sucks. Disabling all API Keys")

    dncValid = False
    dncValidSelect = input("Do you have a doNotCall ApiKey (yes/no)? ").strip()
    dncApi = ""
    if "yes" in dncValidSelect.lower():
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
    variableInfo2 = 'weatherInfo = {"language" : "english", "lang" : "en", "units": "e", "callback": "test", "mode":"JSON", "types": "link, accurate", "measurement":"imperial", "count": "10"} # Can change measurement to metric")'
    f.write(variableInfo)
    f.write(variableInfo2)
    f.flush()
    f.close()

def printLogo():
    f = open("AsciiLogo.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line.strip())
    f.close()
#    input()

def createRequirements():
    print("Here we select what we want to add to the requirements. Some people don't want to dowload everything")
    print("Later on that may become a huge file and nobody wants to waste space")
    print("Options:\n1.All\n2.Minimal\n3.Basic\n4.Speech\n5.Google")
    selection = int(input("Input your selection: "))
    f = open("Data/allRequirements.txt", "r")
    req = open("requirements.txt", "w")
    lines = f.readlines()
    f.close()
    minimal = [2, 3, 13, 18, 20, 35, 38, 44]
    basic = [0, 14, 17, 23, 24, 25, 27, 29, 30, 31, 40, 45] # Minimal
    speech = [4, 28, 32, 34, 41] # Basic
    google = [1, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 19, 21, 22, 26, 33, 36, 37, 39, 42, 43] # Basic
    downloading = []
    if selection == 1: # Just copy the file
        for line in lines:
            req.write(line)
    if selection >= 2 and selection <= 5: # Incrementally figure it out
        downloading += minimal
        if selection >= 3:
            downloading += basic
            if selection == 4:
                downloading += speech
            if selection == 5:
                downloading += google
        for d in downloading:
            try:
                req.write(lines[d])
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
