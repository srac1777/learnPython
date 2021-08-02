letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
  counter = {}
  for letter in word:
    if letter in word:
      if letter in counter:
        counter[letter] += 1
      else:
        counter[letter] = 1
    else:
      continue
  return len(counter.keys())


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write your count_multi_char_x function here:


def count_multi_char_x(word, x):
  return len(word.split(x))-1


# Uncomment hese function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
  s = word.find(start)
  e = word.find(end)
  if s != -1 and e != -1:
    return word[s+1:e]
  return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
