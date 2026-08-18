arr = [4, 7, 2, 9, 7, 1, 6]

seen = set()
found = False

for num in arr:
    if num in seen:
        found = True
        break
    seen.add(num)

print(found)
