def urlify_in_place(arr, true_len):
	true_len_rem = true_len
	count = 0
	
	while true_len_rem > 0:
		if arr[count] != " ":
			true_len_rem -= 1
			count += 1 
		else:
			arr[count] = '%'
			true_len_rem -= 1
			count, arr = shift_by_two(arr, count, true_len_rem)
	return arr

def shift_by_two(arr, count, true_len_rem):
	end_pos = count + true_len_rem
	start_pos = count + 1
	
	for i in range(end_pos, start_pos - 1, -1):
		arr[i+2] = arr[i]
	
	arr[start_pos] = '2'
	arr[start_pos + 1] = '0'
	return count + 3, arr

print(urlify_in_place(['M','r',' ', 'J','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' '], 13))
print(urlify_in_place(['a',' ','p','p',' ',' '], 4))