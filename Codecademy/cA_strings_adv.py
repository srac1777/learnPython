# Write your check_for_name function here:

def check_for_name(sentence, name):
  s_lower = sentence.lower()
  n_lower = name.lower()

  return s_lower.find(n_lower) > -1


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Write your every_other_letter function here:
def every_other_letter(word):
  res = ""
  for i in range(0, len(word), 2):
    res += word[i]
  return res


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


# Write your reverse_string function here:
def reverse_string(word):
  res = ""
  for i in range(len(word)-1, -1, -1):
    res += word[i]
  return res


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Write your make_spoonerism function here:


def make_spoonerism(word1, word2):
  lw1 = word1[0]
  lw2 = word2[0]

  return lw2+word1[1:]+" "+lw1+word2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
