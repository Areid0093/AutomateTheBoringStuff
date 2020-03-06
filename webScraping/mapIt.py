## Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip, re

addressPattern = re.compile(r'''
    ^([0-9])
    (/)$                    
    ''', re.VERBOSE)

if len(sys.argv) > 1:
    # Grab address from command line
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # Grab address from the clipboard
    address = pyperclip.paste()
    print(pyperclip.paste())
    
webbrowser.open('https://www.google.com/maps/place/' + address)
    