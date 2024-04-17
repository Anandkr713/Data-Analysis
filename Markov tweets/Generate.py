import sys
import os.path
import json
import random


def main():
    length, filename = readArguments()
    dictionary = loadDictionary(filename)

    lastWord = "~~~~~~~~~~~~~~~~~"
    result = ""
    for i in range(0, length):
        newWord = getNextWord(lastWord, dictionary)
        result = result + " " + newWord
        lastWord = newWord

    print(result)

def loadDictionary(filename):
    if not os.path.exists(filename):
        sys.exit("Error 404")

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary


def readArguments():
    length =50
    filename = "dictionary.json"

    numArguments = len(sys.argv) -1
    if numArguments >= 1:
        length = int(sys.argv[1])
    if numArguments >= 2:
        filename = sys.argv[2]

    return length, filename


def getNextWord(lastWord, dict):
    if lastWord not in dict:
        newWord = pickRandom(dict)
        return newWord

    else:
        #pick next word from list
        candidates = dict[lastWord]
        candidatesNormalized = []

        for word in candidates:
            freq = candidates[word]
            for i in range(0, freq):
                candidatesNormalized.append(word)

        rnd = random.randint(0, len(candidatesNormalized) -1)
        return  candidatesNormalized[rnd]




def pickRandom(dict):
    randNum = random.randint(0, len(dict) -1)
    newWord = list(dict.keys())[randNum]
    return newWord


main()