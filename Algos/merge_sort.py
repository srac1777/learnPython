from merge import merge

def MergeSort(l, h, arr):
    if l >= h:
        return [arr[h]]
    if l < h:
        mid = int((l+h)/2)
        left = MergeSort(l, mid, arr)
        right = MergeSort(mid+1, h, arr)
        return merge(left, right)

print(MergeSort(0, 2,[1,1,1]))
