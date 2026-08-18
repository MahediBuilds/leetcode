def checkLeft(arr, idx):
    i = idx
    while i > 0:
        if arr[i] < arr[i - 1]:
            swap(i, i - 1, arr)
        i -= 1


def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


arr = [5, 2, 8, 1, 3]

for i in range(1, len(arr)):
    checkLeft(arr, i)

print(arr)
