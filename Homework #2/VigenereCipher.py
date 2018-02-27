"""
Program: VigenereCipher.py
Author: Andrew Walker
Description: Takes a file and encrypts or decrypts it using Vigenere-cypher keyword
"""

from os.path import exists

CHARACTER_OFFSET_DICT = {'a':0, 'b':1, 'c':2, 'd':3,'e':4, 'f':5, 'g':6, 'h':7,'i':8, 'j':9, 'k':10,'l':11, 'm':12,
                          'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
                          'y':24, 'z':25, ' ':26, '\n':27, ',':28, '.':29, '?':30, '!':31}


def main():
    task = getTask()
    file = getFile(task)

    # if user wants to encrypt
    if task == 'n':
        zzzVersion = file[:-4] + ".zzz" # name of the encrypted file we will create
        while exists(zzzVersion): # if we're about to overwrite a file, asks the user if they're sure
            overwrite = input("%s already exists! Would you like to overwrite it? (y/n): " % zzzVersion)
            if overwrite.lower() == 'y':
                break
            else:
                file = getFile(task)
        keyword = input("What keyword would you like to encrypt with?: ")
        encrypt(file, keyword)
    # if user wants to decrypt, if user wanted to exit they will never get here
    else:
        txtVersion = file[:-4] + ".txt"  # name of the decrypted file we will create
        while exists(txtVersion):
            overwrite = input("%s already exists! Would you like to overwrite it? (y/n): " % txtVersion)
            if overwrite.lower() == 'y':
                break
            else:
                file = getFile(task)
        keyword = input("What keyword would you like to decrypt with?: ").lower()
        decrypt(file, keyword)



def getTask():
    """ Asks what the user would like to do, checks to see if it's valid input, and returns it """
    acceptedTasks = ['n', 'd', 'x']
    task = input("Do you want to encrypt a file, decrypt a file, or exit? (enter n, d, or x): ")
    while task not in acceptedTasks:
        print("Input must be n for encrypt, d for decrypt, or x for exit.")
        task = input("Do you want to encrypt a file, decrypt a file, or exit? (enter n, d, or x): ")
    if task == 'x':
        print("Thank you for using VigenereCipher.py")
        exit()
    else:
        return task

def getFile(task):
    """ Further asks what file the user would like to modify, ensures it's a valid file, and returns it"""
    if task == 'n':
        file = input("What file would you like to encrypt?: ")
        while not exists(file) or (file[-4:] != '.txt'): # checks to make sure file exists and in the right format
            if not exists(file): # lets the user know the file failed because it didn't exist
                print("This file does not exist.")
            if file[-4:] != '.txt': # lets the user know the file failed because it didn't end in '.txt'
                print("The file must end in '.txt'.")
            file = input("What file would you like to encrypt?: ")
        return file

    if task == 'd':
        file = input("What file would you like to decrypt?: ")
        while not exists(file) or (file[-4:] != '.zzz'): # checks to make sure file exists and in the right format
            if not exists(file): # lets the user know the file failed because it didn't exist
                print("This file does not exist.")
            if file[-4:] != '.zzz': # lets the user know the file failed because it didn't end in '.zzz'
                print("The file must end in '.zzz'.")
            file = input("What file would you like to decrypt?: ")
        return file

def keyFromValue(value, dictionary):
    """ Searches a dictionary and returns the first key that has the given value"""
    for key in dictionary:
        if dictionary[key] == value:
            return key


def encrypt(file, keyword):
    """ Takes in a .txt file and keyword, encrypts using a Vigenere Cipher, and writes it in a new .zzz file """
    fileToEncrypt = open(file, 'r')
    encryptedFile = open((file[:-4] + '.zzz'),'w')
    keywordLength = len(keyword)
    keywordNumDict = {} # contains the offsets from the keyword

    # creates offset dictionary from keyword
    pos = 0
    for char in keyword:
        keywordNumDict[pos] = CHARACTER_OFFSET_DICT[char]
        pos += 1

    count = 0 # count % 'keywordLength' will be the current letter of the keyword we want to use to encrypt a letter
    stringFileToEncrypt = fileToEncrypt.read()
    for letter in stringFileToEncrypt:
        keywordCyclePosition = count % keywordLength
        letter = letter.lower()
        if letter in CHARACTER_OFFSET_DICT:
            encryptedLetter = (CHARACTER_OFFSET_DICT[letter] + keywordNumDict[keywordCyclePosition]) % 32
            encryptedFile.write(keyFromValue(encryptedLetter, CHARACTER_OFFSET_DICT))
            count += 1



def decrypt(file, keyword):
    """ Takes in a .zz file and keyword, decrypts using a Vigenere Cipher, and writes it in a new .txt file """
    fileToDecrypt = open(file, 'r')
    decryptedFile = open((file[:-4] + '.txt'), 'w')
    keywordLength = len(keyword)
    keywordNumDict = {}  # contains the offsets from the keyword

    # creates offset dictionary from keyword
    pos = 0
    for char in keyword:
        keywordNumDict[pos] = CHARACTER_OFFSET_DICT[char]
        pos += 1

    count = 0  # count % 'keywordLength' will be the current letter of the keyword we want to use to encrypt a letter
    stringFileToDecrypt = fileToDecrypt.read()
    for letter in stringFileToDecrypt:
        keywordCyclePosition = count % keywordLength
        letter = letter.lower()
        if letter in CHARACTER_OFFSET_DICT:
            decryptedLetter = (CHARACTER_OFFSET_DICT[letter] - keywordNumDict[keywordCyclePosition] + 32) % 32
            print(CHARACTER_OFFSET_DICT[letter], keywordNumDict[keywordCyclePosition], decryptedLetter)
            decryptedFile.write(keyFromValue(decryptedLetter, CHARACTER_OFFSET_DICT))
            count += 1

# allows the user to encrypt/decrypt files for as long as they want
# to exit, user enters 'x'
while True:
    main()

print("Thank you for using VigenereCipher.py")