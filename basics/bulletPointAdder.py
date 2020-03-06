## Adds Wikipedia bullet points to the start
## of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
# Loop through all indexes in the "lines" list
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # Add star to each string in the "lines" list
    
text = '\n'.join(lines)
pyperclip.copy(text)