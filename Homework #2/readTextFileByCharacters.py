"""
    File:  readTextFileByCharacters.py
    Description:  Simple program to demonstrate how to:
    * read a text file as a single string
    * process each character by echoing it to the screen
"""
from os.path import exists

def main():
    fileName = input("Enter file name to split into words: ")

    if not exists(fileName):
        print("File", fileName, "does NOT exist!")
    else:
        # Open the file for reading 'r'
        myFile = open(fileName, 'r')
        # read whole file into a single string!
        stringOfFile = myFile.read()
        # loop over the string a character at a time
        for ch in stringOfFile:
            print(ch,end="")
            
main()
