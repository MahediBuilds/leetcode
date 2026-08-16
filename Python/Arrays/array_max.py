arr = [4, 7, 2, 9, 1, 6]
max = 0

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print(max)