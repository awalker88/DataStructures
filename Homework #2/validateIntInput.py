"""
    File:  validateIntInput.py
    Author: Dr. Mark Fienup
    Description:  Simple program to demonstrate try-except to validate
    an integer input from the user.   
"""

def main():

    while True:
        try:  # tries to convert input string to an int, but if it fails
              # do "except" code; otherwise break out of the loop
            number = int(input("Enter an integer: "))
            break  # only gets here if the conversion to an int was successful
        except:
            print("Invalid integer! Please retry.")


main()
