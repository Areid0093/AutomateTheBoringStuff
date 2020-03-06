##  Renames filenames with European DD-MM-YYYY date format to American MM-DD-YYYY.

import shutil, os, re

## Regex to match European date format

datePattern = re.compile(r'''^(.*?)
    ((0|1|2|3)?\d)-
    ((0|1)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

## Loop over files within current working directory

for euroFilename in os.listdir('.'):
    ## Skip files that don't match date regex
    if (mo := datePattern.search(euroFilename)) == None:
        continue
    ## Select desired parts of the file name
    beforePart = mo.group(1)
    dayPart = mo.group(2)
    monthPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    ## Create American date format
    amFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart
    ## Get absolute file paths
    absWorkingDir = os.path.abspath('.')
    amFilename = os.path.join(absWorkingDir, amFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    ## Rename files
    print('Renaming "%s" to "%s"...' % (euroFilename, amFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing