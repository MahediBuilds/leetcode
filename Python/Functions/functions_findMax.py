def find_max(arr):
    largest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
    
    return largest

arr = [4, 7, 2, 9, 1, 6]
print(find_max(arr))