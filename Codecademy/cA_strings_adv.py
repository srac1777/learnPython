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
