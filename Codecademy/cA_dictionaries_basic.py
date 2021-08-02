# Write your sum_values function here:
def sum_values(m):
  vals = list(m.values())
  return sum(vals)


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# Write your sum_even_keys function here:
def sum_even_keys(d):
  total = 0
  for key in d.keys():
    if key % 2 == 0:
      total += d[key]
  return total


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6


# Write your add_ten function here:
def add_ten(d):
  for key in d.keys():
    d[key] += 10
  return d


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}


# Write your values_that_are_keys function here:
def values_that_are_keys(d):
  l = []
  for v in d.values():
    if d.get(v):
      l.append(v)
  return l


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]


# Write your max_key function here:
def max_key(d):
  keys = list(d.keys())
  max = keys[0]
  for key in keys:
    if d[key] > d[max]:
      max = key
  return max


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"
