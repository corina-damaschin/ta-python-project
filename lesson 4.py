print('You are in Master Branch!')

#emoji module
from emoji import emojize
print(emojize(':angry_face_with_horns:'))


f = open('doc.txt', 'r')
print(f.read(156))
for line in f:
    print(line.strip())
f.close()

f = open('doc.txt', 'r')
print(f.read(156))
for line in f:
    print(line, end="")
f.close()

file = open("doc.txt", "r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
print("\nThis is the number of lines in the file 'doc.txt'")
print(Counter)

lst = ['Bananas', '&', 'Coconuts']
f = open('tropic.txt','w')
for l in lst:

    f.write(l)
f.close()

from datetime import (datetime, date)
print(datetime.today())
print(date.today())