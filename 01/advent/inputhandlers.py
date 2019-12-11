import re

def LoadMockInput():
    return [
        12,
        14,
        1969,
        100756
    ]

def LoadInputFromFile(filename):
    inputList = []

    file = open(filename, "r")

    for line in file:
        # clear extra chars besides digits
        line = re.sub("[^0-9]", "", line)

        # add to our list
        inputList.append(int(line))

    file.close()

    return inputList
