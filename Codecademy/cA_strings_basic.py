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
