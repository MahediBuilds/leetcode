numbers = [1, 2, 2, 3, 1, 4, 3, 5, 5]

numSet = set()
for num in numbers:
    if num not in numSet:
        numSet.add(num)
print(numSet)
