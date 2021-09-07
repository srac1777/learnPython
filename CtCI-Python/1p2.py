def check_permutation(a, b):
    if len(a) != len(b):
        return False
    
    hshA = construct_hash(a)
    hshB = construct_hash(b)
	
    for k in hshA:
        if k not in hshB or hshA[k] != hshB[k]:
            return False
    return True

def construct_hash(str):
	res = {}
	for ch in str:
		if ch in res:
			res[ch] += 1
		else:
			res[ch] = 1
	return res

print(check_permutation("ab", "ba"))
print(check_permutation("abr", "bap"))
print(check_permutation("absdfasf", "ba"))
print(check_permutation("", "ba"))
print(check_permutation("", ""))
print(check_permutation("pop", "opp"))
