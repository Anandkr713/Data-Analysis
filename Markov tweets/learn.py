import sys
import os.path
import json
def main():
    dictionaryFile, inputFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)

    if inputFile == "":
        # interactive mode
        while True:
            userInput = input(">> ")
            if userInput == "":
                break

            dictionary = learn(dictionary, userInput)
            updateFile(dictionaryFile,dictionary)

    else:
        #readfile
        print("Not yet implemented")


def updateFile(filename, dictionary):
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()

def loadDictionary(filename):
    if not os.path.exists(filename):
        file = open(filename, "w")
        json.dump( {}, file)
        file.close()

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary

def readArguments():
    numArguments = len(sys.argv) -1

def readArguments():
    numArguments = len(sys.argv) -1
    dictionaryFile = "dictionary.json"
    inputFile = ""

    if numArguments >= 1:
        dictionaryFile = sys.argv[1]
    if numArguments >= 2:
        inputFile = sys.argv[2]

    return dictionaryFile, inputFile

def learn(dict, input):
    tokens = input.split(" ")
    for i in range(0, len(tokens)-1):
        currentWord = tokens[i]
        nextWord = tokens[i+1]

        if currentWord not in dict:
            # create a new entry in dictionary
            dict[currentWord] = { nextWord : 1 }
        else:
            # current word already exists
            allNextWords = dict[currentWord]

            if nextWord not in allNextWords:
                # add new next state
                dict[currentWord][nextWord] = 1
            else:
                # exists, increment
                dict[currentWord][nextWord] = dict[currentWord][nextWord]+1

    return dict


main()