arr = [2, 7, 11, 15]
target = 9

seen = set()

for num in arr:
    x = target - num

    if x in seen:
        print(num, x)
        break
    seen.add(num)
