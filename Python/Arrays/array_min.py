arr = [10, 3, 7, 2, 8, 5]

smallest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element:", smallest)