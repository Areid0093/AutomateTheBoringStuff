## Check password input to see whether or not it satisfies the following:
## Password must contain at least one uppercase, one lowercase, one digit, 
## One special character, and at least 8 characters minimum

import re

pwRegex = re.compile(r'''(
    (?=.*?[A-Z])            # check for uppercase letter
    (?=.*?[a-z])            # check for lowercase letter
    (?=.*?[0-9])            # check for digit
    (?=.*?[^a-zA-Z0-9])     # check for special character
    [a-zA-Z0-9.-]{8,}       # check for at least 8+ characters
    )''', re.VERBOSE)

def pwCheck():
    pw = input('Please enter a password: ')
    if mo := pwRegex.search(pw):
        return True
    else:
        print('Try again')
        return False
   
pwCheck()
    


    