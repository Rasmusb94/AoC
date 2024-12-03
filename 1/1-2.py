import os

inputlist = open('input.txt', 'r')
content = inputlist.read()
list1 = []
list2 = []
currentNumber = 0
result = content.split( )

for x in result:
    if currentNumber % 2 == 0:
        list1.append(int(x))
    else:
        list2.append(int(x))
    currentNumber += 1

totalScore = 0

for x in list1:
    numOccurances = 0
    for y in list2:
        if x == y:
            numOccurances += 1
    totalScore += (x * numOccurances)

print(totalScore)