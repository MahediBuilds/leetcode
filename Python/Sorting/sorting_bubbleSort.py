arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j + 1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)
