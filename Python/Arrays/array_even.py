arr = [4, 7, 2, 9, 1, 6]

count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1

print("Count of even numbers:", count)