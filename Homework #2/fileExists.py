"""
    File:  fileExists.py
    Author: Dr. Mark Fienup
    Description:  Simple program to demonstrate the os.path module function
    "exists" which checks to see if the file name exists.
"""
from os.path import exists
import os

def main():
    # Display contents of the current directory
    directoryList = os.listdir('.')  # '.' indicates the current directory
    print("The contents of the current directory are:")
    for dirItem in directoryList:
        print(dirItem)
    print()

    while True:
        fileName = input("Enter file name to search for (or <Enter> to exit): ")
        if fileName == '':
            break
        elif exists(fileName):
            print(fileName, "exists!")
        else:
            print(fileName, "does NOT exist!")
main()
