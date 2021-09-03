def is_unique(str):
    hsh = {}
    for ch in str:
        if ch in hsh:
            return False
        else:
            hsh[ch] = True
    return True

print(is_unique("apple"))
print(is_unique("aple"))
print(is_unique("aaaa"))
print(is_unique("pen"))
print("======================================")
def is_unique_no_ds(str):
    if len(str) == 1:
        return True
    for i in range(0, len(str)-1):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return False
    return True


print(is_unique_no_ds("apple"))
print(is_unique_no_ds("aple"))
print(is_unique_no_ds("a"))
print(is_unique_no_ds("pen"))
