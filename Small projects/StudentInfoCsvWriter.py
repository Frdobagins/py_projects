#take input student name, credit hours, hours studied, favorite study spot
newStudent = []

def addStudent(): 
    '''Get Student Info'''
    studentInfo = [input("Name? "), int(input("Credit Hours? ")), int(input("Hours Studied? ")), input("Favorite Styudy Spot? ")]
    return studentInfo
    ### Retry input if type is wrong, raise an exception instead of causing an error############

#format input (function)
def inputPrep(upi):
    '''format the info'''
    upi = str(upi)
    upi = upi.lower()
    upi = upi.capitalize()
    upi = str(upi)
    upi = upi.strip()
    return str(upi)
    ### IDK what is happeneing here ##############################################################3

def csvify(alist):
    '''format and prep info for csv'''
    goodStr = ""
    for i in range(len(alist)):
        temp = str(alist[i])
        goodStr = goodStr + temp + ","
    goodStr = goodStr + "\n"
    return goodStr

def decsvify(line):
    '''replaces commas with new lines'''
    workingLine = line.split(",")
    deflst = ""
    for i in workingLine:
        deflst = deflst + i + '\n'
    return deflst

#open file
def appendtoFile(lst):
    '''Append info to end of file if there is new info'''
    if lst != []:
        with open("sStorage.csv", "a") as ssFile:
            ssFile.write(csvify(lst))
            ssFile.close()
    else:
        print("no info, submit info first")

def printFromFile(start=0, stop=False):
    with open("sStorage.csv") as ssFile:
        wholeFile = ssFile.readlines()
        if not stop:
            stop = len(wholeFile)
        for i in range(start, stop):
            print(decsvify(wholeFile[i]))
        ssFile.close()

def startLoop():
    while True:
        print("\n")
        prompt1 = str(input("Add Student? (Press enter to decline)"))
        if prompt1 != "" and prompt1.lower() != "no":
            newStudent = addStudent()
            appendtoFile(newStudent)
            newStudent = []
        else:
            print("You declined")
        print("\n")
        prompt2 = str(input("print file?"))
        if prompt2 != ""  and prompt2.lower() != "no":
            printFromFile()
        else:
            print("You Declined")
        prompt3 = str(input("Are you done with the File? (type yes to be done)"))
        if prompt3.lower() == "yes":
            print("Exiting")
            break

def main():
    startLoop()

main()