"""
File: textEditor.py
Author: Andrew Walker
Date: 3/3/2018
Description:
"""
from os.path import exists, getsize
from time import sleep

from cursor_based_list import CursorBasedList

def main():
    filename = input("Please enter a .txt filename: ")
    loadedCBL = fileLoader(filename)
    menuOptions(loadedCBL, filename)

def fileLoader(filename):
    """Takes a string filename as only argument
        If file exists: adds it line by line
        If file does not exist: create empty CursorBasedList object"""
    while filename[-4:] != ".txt":
        print("File must be a .txt file")
        filename = input("Please enter a .txt filename: ")

    newCBL = CursorBasedList()

    if exists(filename):
        toOpenFile = open(filename, 'r')
        if getsize(filename) == 0:
            newCBL = initialize(newCBL) # allows us to assume that there is at least one object in the CBL
        else:
            for line in toOpenFile:
                line = line.rstrip()  # ensures there's no newline so we can safely add one
                line += "\n"
                newCBL.insertAfter(str(line))
        return newCBL # new linked list object filled with .txt file's lines
    else:
        newCBL = initialize(newCBL)
        save(newCBL, filename)
    return newCBL  # new empty linked list object

def initialize(emptyCBL):
    """ Takes in an empty cursor_based_list and initializes it with a user entry """
    firstEntry = input("Initialize your new text file with a first entry (can be changed later): ")
    firstEntry = firstEntry.rstrip("\n")  # ensures there's no newline so we can safely add one
    firstEntry += "\n"
    emptyCBL._current = emptyCBL._header # sets the header to current since current is initially 'none'
    emptyCBL.insertAfter(firstEntry)
    return emptyCBL

def save(CBL, filename):
    """ Saves the contents of our cursor based list back to the opened file """
    fileToWrite = open(filename, 'w')
    current = CBL._header.getNext()
    while current.getNext() is not None:
        fileToWrite.write(current.getData())
        current = current.getNext()

def findWord(CBL, word):
    """ Given a word, this searches through the file and returns the number of times and the line(s) the word appears on """
    myCBL = CBL
    linesWithWord = [] # list containing the lines the word occurs on
    linesWithWordNumber = [] # list containing the line number the word occurs on
    numFound = 0

    current = myCBL._header.getNext()
    lineNum = 1
    while current.getNext() is not None:
        lineLst = (str(current.getData())).split() # contains a list of all the words in a line

        if word in lineLst:
            newLineLst = [x if x != word else ("[" + word + "]") for x in lineLst] # adds brackets around the word we're looking for
            newLineStr = ' '.join(newLineLst)
            linesWithWord.append(newLineStr)
            linesWithWordNumber.append(lineNum)
            numFound += 1
        lineNum += 1
        current = current.getNext()
    if len(linesWithWord) == 0:
        print("\nWord not found!")
    else:
        print("")
        print("Word found %s times." % numFound)
        for index in range(0, len(linesWithWord)):
            print("Line %s: %s" % (str(linesWithWordNumber[index]), str(linesWithWord[index])))


def menuOptions(loadedCBL, filename):
    """ Prints menu options and picks which function(s) to run based on user response """
    myList = loadedCBL
    myFile = filename

    while True:
        print("\n===============================================================")
        print("File Contents:\n", myList)
        if myList.isEmpty():
            print("Empty File")
        else:
            print('')
            print("length:", len(myList), " Current line:", myList.getCurrent())
        print("\nMenu Options:")
        print("A - Insert Line After Current Line")
        print("B - Insert Line Before Current Line")
        print("D - Delete Current Line")
        print("F - View First Line")
        print("I - Find Word in File")
        print("L - View Last Line")
        print("N - View Next Line")
        print("P - View Previous Line")
        print("R - Replace the Current Line With a New One")
        print("S - Save the Current List back to the Text File")
        print("X - Exit (will save current list back to text file)")

        response = input("Menu Choice? ").upper()
        if response == 'A':
            # insert a new line after the current one and make it the current line
            item = input("Enter the new line to insertAfter: ") + '\n'
            myList.insertAfter(item)
        elif response == 'B':
            # insert a new line before the current one and make it the current line
            item = input("Enter the new item to insertBefore: ") + '\n'
            myList.insertBefore(item)
        elif response == 'D':
            # delete current line and set current line accordingly
            if myList.isEmpty():
                print("\nYou can not delete the current line because there are no lines.")
                sleep(1.5) # gives user time to read error message
            else:
                item = myList.remove()
                print("item removed:", item)
        elif response == 'F':
            # Navigate to the first line and display it, make it the current line
            if myList.isEmpty():
                print("\nYou can not display the first line because there are no lines.")
                sleep(1.5)
            else:
                myList.first()
                print(myList._current.getData())
        elif response == "I":
            # Searches for word and prints the number of times and line(s) it appears on
            word = input("What word would you like to find?: ")
            findWord(myList, word)
            sleep(1.5)
        elif response == 'L':
            # Navigate to the last line and display it, make it the current line
            if myList.isEmpty():
                print("\nYou can not display the last line because there are no lines.")
                sleep(1.5)
            else:
                myList.last()
                print(myList._current.getData())
        elif response == 'N':
            if myList.isEmpty():
                print("\nYou can not display the next line because there are no lines.")
                sleep(1.5)
            elif myList._current.getNext() == myList._trailer:
                print("\nThere is no next line!")
                sleep(1.5)
            else:
                myList.next()
                print(myList._current.getData())
        elif response == 'P':
            if myList.isEmpty():
                print("\nYou can not display the previous line because there are no lines.")
                sleep(1.5)
            elif myList._current.getPrevious() == myList._header:
                print("\nThere is no previous line!")
                sleep(1.5)
            else:
                myList.previous()
                print(myList._current.getData())
        elif response == 'R':
            if myList.isEmpty():
                print("\nYou can not replace the current line because there are no lines.")
                sleep(1.5)
            else:
                item = input("Enter replacement item: ")
                item = item.strip() + "\n"
                myList.replace(item)
                print(myList._current.getData())
        elif response == 'S':
            save(myList, myFile)
        elif response == 'X':
            likeToSave = input("Would you like to save your file before you exit? (Y/N): ")
            likeToSave = likeToSave.lower()
            if likeToSave == 'y':
                save(myList, myFile)
            break
        else:
            print("\nInvalid Menu Choice!")
            sleep(1.5)

main()
