import re

## Basic RegEx search/match
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
mo.group(2)

## Matching multiple groups with '|'
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

## Optional matching with '?'
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

## Optional matching with '?'
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()

## Matching zero or none with '*'
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()


## Matching one or more with '+'
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

## Matching specific repetitions with '{}'
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
mo2 = haRegex.search('Ha')
mo2 == None

## Greedy & Non-greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

## Findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

## Shorthand character classes
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

## Creating own character ckasses
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('Robocop eats baby food. BABY FOOD.')

## ^ and $ characters
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12 34567890') == None

## Wilcard character '.'
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

## Matching everything with '.*'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)\
    
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

## Matching newlines with '.'
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

## Case-insensitive matching
regex1 = re.compile('Robocop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

## Substituting strings with the sub() method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

## Managing complex RegEx
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

## Combining RegEx
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
    