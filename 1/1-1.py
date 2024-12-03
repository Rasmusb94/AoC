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

list1.sort()
list2.sort()

totalDifference = 0
counter = 0

while counter < len(list1):
    num1 = list1[counter]
    num2 = list2[counter]
    if list1[counter] != list2[counter]:
        if num1 > num2:
            totalDifference += num1 - num2
        else:
            totalDifference += num2 - num1
    counter += 1

print(totalDifference)