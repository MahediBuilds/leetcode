arr = [4, 7, 2, 9, 1, 6]

largest = arr[0]
second_largest = largest
for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
        
        
print(second_largest)