##  Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

## Regex to match American date format

datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

## Loop over files within current working directory

for amFilename in os.listdir('.'):
    ## Skip files that don't match date regex 
    if (mo := datePattern.search(amFilename)) == None:
        continue
    ## Select desired parts of the file name
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    ## Create European date format
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    ## Get absolute file paths
    absWorkingDir = os.path.abspath('.')
    amFilename = os.path.join(absWorkingDir, amFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    ## Rename files
    print('Renaming "%s" to "%s"...' % (amFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing