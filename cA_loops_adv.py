#Write your function here
def larger_sum(lst1, lst2):
  sum1 = cal_sum(lst1)
  sum2 = cal_sum(lst2)

  if sum1 >= sum2:
    return lst1
  else:
    return lst2

def cal_sum(lst):
  count = 0
  for item in lst:
    count += item
  return count

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  i = 0
  while i < len(lst) and sum <= 9000:
    sum += lst[i]
    i += 1
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here


def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


#Write your function here
def same_values(lst1, lst2):
  sv = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      sv.append(i)
  return sv


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


#Write your function here
def reversed_list(lst1, lst2):
  reversed = True
  for i in range(len(lst1)):
    if lst2[i] != lst1[len(lst1)-1-i]:
      reversed = False
      break
  return reversed


#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
