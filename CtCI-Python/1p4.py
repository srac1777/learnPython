def construct_hash(str):
    hsh = {}

    for ch in str:
        if ch != ' ':
            if ch in hsh:
                hsh[ch] += 1
            else:
                hsh[ch] = 1

    return hsh

def truelen(str):
    count = 0
    for ch in str:
        if ch != ' ':
            count +=1
    return count

def palindrome_permutation(str):
	if truelen(str) < 2:
		return True
	
	counter_hash = construct_hash(str) #ignore whitespaces
	
	if truelen(str) % 2 == 0:
		return check_even_len(counter_hash)
	else:
		return check_odd_len(counter_hash)

def check_even_len(hsh):
	for k, v in hsh.items():
		if v % 2 != 0:
			return False
	return True

def check_odd_len(hsh):
    hasOdd = False
    for k,v in hsh.items():
        if v % 2 !=0 and not hasOdd:
            hasOdd = True
        elif v % 2 != 0 and hasOdd:
            return False
        else:
            continue
    return True


		
print(palindrome_permutation("mom"))  # true
print(palindrome_permutation("mo m"))  # true
print(palindrome_permutation("moom"))  # true
print(palindrome_permutation("mopm"))  # false
print(palindrome_permutation("mom om")) # true
print(palindrome_permutation("momom")) # true
print(palindrome_permutation("msdfh")) # false
