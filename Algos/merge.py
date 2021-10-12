def merge(list1, list2):
    i, j = 0, 0
    res = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    
    while i < len(list1):
        res.append(list1[i])
        i += 1
    
    while j < len(list2):
        res.append(list2[j])
        j += 1
    
    return res


list1 = [0]
list2 = [1,2,2,4,7,19,23,77,91, 99, 101]
# print(merge(list1, list2))