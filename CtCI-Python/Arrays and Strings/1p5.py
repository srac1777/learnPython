def one_away(strA, strB):
	if strA == strB:
		return True
	if abs(len(strA) - len(strB)) > 1:
		return False

	if len(strA) == len(strB):
		return check_one_away_eq(strA, strB)
	else:
		return check_one_away_uneq(strA, strB)


def check_one_away_eq(strA, strB):
	diff = False
	for i in range(len(strA)):
		if strA[i] == strB[i]:
			continue
		elif strA[i] != strB[i] and diff == False:
			diff = True
		else:
			return False
	return True


def check_one_away_uneq(strA, strB):
    diff = False
    str_to_iterate, other_string = get_string_to_iterate(strA, strB)
    j = 0
    for i in range(len(str_to_iterate)):
        if str_to_iterate[i] == other_string[j]:
            j += 1
            continue
        elif str_to_iterate[i] != other_string[j] and diff == False:
            diff = True
            j += 2
        else:
            return False
    return True


def get_string_to_iterate(A, B):
	if len(A) > len(B):
		return B, A
	else:
		return A, B


print(one_away("pale", "bale"))
print(one_away("pale", "pales"))
print(one_away("pale", "ple"))
print(one_away("pale", "bake"))
print(one_away("pale", "be"))
