import subprocess
import getpass

#######################
# Launching Softwares #
#######################
def launch(program):
    f = open("Data/Application.txt", "r")
    username = getpass.getuser()
    lines = f.readlines()
    size = len(lines)
    for i in range(0, size): # CLEANING THE FUCKING \n off
        lines[i] = lines[i].strip().lower()
    f.close()

    f1 = open("Data/Paths.txt", "r")
    lines1 = f1.readlines()
    size = len(lines1)
    for i in range(0, size): # CLEANING FOR USER SPECIFIC
        lines1[i] = lines1[i].strip().replace("%USER%",username)
    f1.close()

    ## WILL HAVE ISSUES IF REQUIRE ADMIN
    ## ALSO ADD IF CLOSE TO IT
    ## ADD LOWERCASE TO MATCH
    ## Add that adding new ones
    ## Fill out the microsoft Store apps
    ind = -1
    program = program.lower()
    if program in lines:        
        ind = lines.index(program)
    if ind < 0:
        return False
    try:
        subprocess.Popen(lines1[ind])
    except:
        print("That may require elevated permissions. I cannot open it")
        return False
    return True
