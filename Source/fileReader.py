from addition import addition
import pprint


def readFile(fileName):
    """ reads in the file, reads every line in the file using readLines
    RETURNS 'What is $X + $Y equal to?'
    """
    file = open(fileName, 'r')
    contentFile = file.readlines()

    return contentFile[0]


def identifyVariables(question):
    """identifies the variables in the question"""
    variables = []
    dictOfVars = {}
    # splits it up into words
    for i in question.split(" "):
        # if word starts with $, it's a variable
        if i[0] == "$":
            variableName = i.split('$')[1]
            variables.append(variableName)
            dictOfVars[variableName] = ""

    if len(question.split("{")) > 1:
        hiddenConstantsString = question.split("{")[1].split("}")[0]
        for constantDefinitions in \
                hiddenConstantsString.replace(' ', '').split(","):
            dictOfVars[constantDefinitions.split("=")[0]] \
                = constantDefinitions.split("=")[1]

    return dictOfVars


def writeQuestion(question, answer, dictVariables):
    # TODO Make this code work for multiple types of questions
    returnString = []

    if len(question.split("{")) > 1:
        question = question.split("{")[0] + question.split("}")[1]

    file_read = question.split(" ")
    for value in file_read:
        if value[0] != "$":
            returnString.append(value)
        else:
            for i in dictVariables:
                if value[1::] == i:
                    returnString.append(dictVariables[i])
    returnString.append("\n " + str(answer))

    return " ".join(str(x) for x in returnString)


a = readFile('example1.txt')
print("readFile is equal to", a)

varDict = addition.generateNumbers(identifyVariables(a))
b, c = addition.generate(identifyVariables(a))
pprint.pprint(b)
print("userChangeVariables is equal to", c)

question_complete = writeQuestion(a, c, b)
print(question_complete)
