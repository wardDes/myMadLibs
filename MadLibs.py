from pathlib import Path
import pyinputplus as pyip
import re

spchprtsrgx = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

p = Path.cwd()

print('Enter name of madlib file text file')
txtfile = pyip.inputFilename()


madlib1File = open(p/txtfile)
madlib1Content = madlib1File.read()
madlib1File.close()


mo = spchprtsrgx.findall(madlib1Content)


for i in mo:
    print(f'Enter a {i}')
    response = input()
    print(i, response)
    madlib1Content = madlib1Content.replace(i, response, 1)


newMadLibFile = open(p/('completed_' + txtfile ), 'w')
newMadLibFile.write(madlib1Content)
print(madlib1Content)
newMadLibFile.close()
