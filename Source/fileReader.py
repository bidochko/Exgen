import random
def readFile(fileName):
    # reads in the file, reads every line in the file using readLines
    # RETURNS 'What is $X + $Y equal to?'
    file = open(fileName, 'r') 
    contentFile = file.readlines()
    
    return contentFile[0]

def identifyVariables(question):
    # identifies the variables in the question
    variables = []
    dictOfVars = {}
    # splits it up into words
    for i in question.split(" "):
        # if word starts with $, it's a variable
        if i[0] == "$":
            variables.append(i)
            # creates a dict of variables and randomly assigns it a num between 1 and 50
            # this number isn't set in stone and is meant to be set by the user somehow
            dictOfVars[i[1::]] = random.randint(1, 50)
    return dictOfVars

def userChangeVariables(dictOfVars):
    # THIS IS THE USERS CODE
    # this is what they've written they want their code to do
    returnVal = dictOfVars['Y'] + dictOfVars['X']
    return returnVal

def writeQuestion(question, answer, dictVariables):
    # TODO find some way so the user doesnt have to rewrite what the variables are here :)
    returnString = []
    file_read = a.split(" ")
    for value in file_read:
        if value[0] != "$":
            returnString.append(value)
        else:
            if value[1] == "X":
                returnString.append(dictVariables['X'])
            if value[1] == "Y":
                returnString.append(dictVariables['Y'])
    returnString.append("\n " + str(answer))            


    return " ".join(str(x) for x in returnString)


a = readFile('example1.txt')
print("readFile is equal to", a)
b = identifyVariables(a)
import pprint
pprint.pprint(b)
c = userChangeVariables(b)
print("userChangeVariables is equal to", c)

question_complete = writeQuestion(a, c, b)
print(question_complete)
