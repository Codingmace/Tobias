import os
#from PAPI.quickstart import main


###########################
#     gmailCleanv1.py     #
# Cleaning out Reply only #
# and safely Unsubscribe  #
# from emails. Clean more #
# in version 2            #
###########################
def gmailCleanup():
    from PAPI import gmailCleanv1
    return cleanGmail()

def imageCleanup():
    print("For compressing images")

def incrementCleanup():
    print("Turning zip into incremental Backups")


#####################
#    OpenCam.py     #
# Open main website #
# to any traffic    #
# Camera in the USA #
#####################
def trafficCamera(query):
    from PAPI.openCam import findWebCamera
    return findWebCamera(query)

#####################
# launchSoftware.py #
# Launches an app   #
# (Path hardcoded)  #
#####################
def openSoftware(query):
    from PAPI.launchSoftware import launch
    softwareExist = launch(query)
    return softwareExist

#####################
#   uniqueLines.py  #
# clean text file   #
# duplicate lines   #
# (And maybe sort)  #
#####################
def unique(query):
    from PAPI.uniqueLines import lineSort, line
    sorting = "sort" in query
    query = query.replace("sort","").strip()
    if not os.path.exists(query):
        return "That file does not exist. Try again"
    if sorting:
        lineSort(query)
    else:
        line(query)
    return "File has been sorted and named newFile.txt"


#####################
#   phoneLookup.py  #
# Used web scraping #
# to get person and #
# place of a number #
#####################
def phoneLookup(query):
    from PAPI.phoneLookup import npnr, USPhonebook
    cleanPhoneNumber = query.replace("[^0-9]", "")
    if len(cleanPhoneNumber) < 10:
        return "The number " + cleanPhoneNumber + " does not have enough numbers"
    site1 = npnr(cleanPhoneNumber)
    site2 = USPhonebook(cleanPhoneNumber)
    if site1 == site2:
        return "I am 100% sure the phone number is " + site1
    elif site1 == "IDK":
        return "There was an issue with site 1, but USPhonebooks said the phone number was " + site2
    else:
        return "I got different results. Site 1 was " + site1 + " and site 2 was " + site2
