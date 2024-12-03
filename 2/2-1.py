completedRuns = 0
totalRows = 0
with open('input.txt', 'r') as file:
    for line in file:
        content = line.rstrip()
        result = content.split( )
        list = []
        for x in result:
            list.append(int(x))
        currentNum = 0
        previousNumber = 0
        increasing = True
        currentListSafe = True
        while currentNum < len(list):
            if currentNum == 0:
                currentNum += 1
                previousNumber = list[0]
                continue
            if currentNum == 1:
                if list[1] - previousNumber > 3 or list[1] - previousNumber < -3 or list[1] == previousNumber:
                    currentListSafe = False
                    break
                if list[1] < previousNumber:
                    increasing = False
                previousNumber = list[1]
                currentNum += 1
                continue
            if increasing == True:
                if list[currentNum] > previousNumber and list[currentNum] - previousNumber <= 3:
                    previousNumber = list[currentNum]
                    currentNum += 1
                    continue
                else:
                    currentListSafe = False
                    break
            else:
                if list[currentNum] < previousNumber and previousNumber - list[currentNum] <= 3:
                    previousNumber = list[currentNum]
                    currentNum += 1
                    continue
                else:
                    currentListSafe = False
                    break
        if currentListSafe == True:
            completedRuns += 1
print(completedRuns)