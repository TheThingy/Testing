import string
from secrets import choice

def passwordGen():

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    finalPassword = ""

    charLength = int(input("Input desired character length:\n"))
    digitLength = int(input("Input desired digit length:\n"))
    specialLength = int(input("Input desired special character length:\n"))
    password = ""
    for i in range(digitLength):
        password += choice(digits)
    for i in range(charLength):
        password += choice(letters)
    for i in range(specialLength):
        password += choice(special)

    for i in range(len(password)):
        finalPassword += choice(password)

    return print(finalPassword)

passwordGen()
