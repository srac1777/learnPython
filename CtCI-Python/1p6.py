def string_compression(in_str):
    if len(in_str) == 1:
        return in_str
    res = []
    curr_letter = in_str[0]
    curr_count = 1

    for i in range(1, len(in_str)):
        if in_str[i] == curr_letter:
            curr_count += 1
        else:
            res.append(curr_letter + str(curr_count))
            curr_letter = in_str[i]
            curr_count = 1

    res.append(curr_letter + str(curr_count))
    final = ''.join(res)
 
    if len(in_str) > len(final):
        return final
    else:
        return in_str

print(string_compression("aabcccaa"))
print(string_compression("aabcccccaaa"))
print(string_compression("aaa"))
print(string_compression("a"))
print(string_compression("ab"))
print(string_compression("abb"))
print(string_compression("AsdjjjjjPOOOMmm"))
