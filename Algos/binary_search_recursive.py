def binary_search_recursive(arr, l, h, key):
    if l > h:
        return None
    if l == h:
        if arr[l] == key:
            return l
        else:
            return None
    else:
        mid = int((l+h)/2)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            return binary_search_recursive(arr, mid+1, h, key)
        else:
            return binary_search_recursive(arr, l, mid - 1, key)
        

arr = [5, 9, 12, 17, 24, 92, 160, 161]
print(binary_search_recursive(arr, 0, len(arr)-1, 160))
