numbers = [1, 2, 2, 3, 1, 2, 4, 3, 1]

myDict = {}

for num in numbers:
    myDict[num] = myDict.get(num, 0) + 1

print(myDict)
