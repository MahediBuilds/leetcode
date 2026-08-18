arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(1, len(arr)):
        if arr[j] > arr[j - 1]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp

print(arr)
