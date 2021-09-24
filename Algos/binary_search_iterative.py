def binary_search_iter(arr, key):
    l = 0
    h = len(arr)-1
    
    while(l <= h):
        mid = int((l+h)/2)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1
    
    return None

arr = [5,9,12,17,24,92,160,161]
print(binary_search_iter(arr, 2))