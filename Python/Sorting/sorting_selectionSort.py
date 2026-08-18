def findSmallest(arr, k):
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i

    return smallest_idx + k


def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    smallest = findSmallest(arr[i : len(arr)], i)
    swap(smallest, i, arr)

print(arr)
