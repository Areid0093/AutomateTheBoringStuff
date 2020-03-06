import re

madLibBase = open('madlibs.txt')
content = madLibBase.read()
lib = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
mo = lib.findall(content)

for i in range(len(mo)):
    libWord = input(f'Please enter a(n) {mo[i]}: ')
    content = lib.sub(libWord, content, 1)
print(content)

madLibBase.close()

