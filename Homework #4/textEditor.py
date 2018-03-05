"""
File: textEditor.py
Author: Andrew Walker
Date: 3/3/2018
Description:
"""
from os.path import exists, dirname, getsize
# from os.stat import

from cursor_based_list import CursorBasedList

"t3"

def main():
    filename = input("Please enter a .txt filename")
    fileLoader(filename)

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
        print(getsize(toOpenFile))
        newCBL._current = newCBL._header # sets the header to current so we can insertAfter
        for line in toOpenFile:
            newCBL.insertAfter(str(line))
        return newCBL # new linked list object filled with .txt file
    else:
        open(filename, 'w')
        firstEntry = input("Initialize your new text file with a first entry (can be changed later): ")
        firstEntry.rstrip("\n") # ensures there's no new line so we can safely add one
        firstEntry += "\n"
        newCBL._current = newCBL._header
        newCBL.insertAfter(firstEntry)
    return newCBL  # new empty linked list object


def testList():
    myList = CursorBasedList()
    myList.insertAfter('a')
    myList.insertAfter('b')
    myList.insertAfter('c')

    while True:
        print("\n===============================================================")
        print("Current List:", myList)
        if myList.isEmpty():
            print("Empty list")
        else:
            print("length:", len(myList), " Current item:", myList.getCurrent())
        print("\nTest Positional List Menu:")
        print("A - Insert Line After Current Line")
        print("B - Insert Line Before Current Line")
        print("C - getCurrent")
        print("F - View First Line")
        print("L - View Last Line")
        print("N - View Next Line")
        print("P - View Previous Line")
        print("R - Remove Current Line")
        print("U - Replace the Current Line With a New One")
        print("S - Save the Current List back to the Text File")
        print("X - Save the Current Line and Exit")

        response = input("Menu Choice? ").upper()
        if response == 'A':
            # insert a new line after the current one and make it the current line
            item = input("Enter the new item to insertAfter: ")
            myList.insertAfter(item)
        elif response == 'B':
            # insert a new line before the current one and make it the current line
            item = input("Enter the new item to insertBefore: ")
            myList.insertBefore(item)
        elif response == 'C':
            #
            item = myList.getCurrent()
            print("The current item in the list is:", item)
        elif response == 'E':
            print("isEmpty returned:", myList.isEmpty())
        elif response == 'F':
            # Navigate to the first line and display it, make it the current line
            myList.first()
        elif response == 'L':
            myList.last()
        elif response == 'N':
            myList.next()
        elif response == 'P':
            myList.previous()
        elif response == 'R':
            item = myList.remove()
            print("item removed:", item)
        elif response == 'U':
            item = input("Enter replacement item: ")
            myList.replace(item)
        elif response == 'X':
            break
        else:
            print("Invalid Menu Choice!")


# testList()

testCBL = fileLoader("sampleText2.txt")
print(testCBL)