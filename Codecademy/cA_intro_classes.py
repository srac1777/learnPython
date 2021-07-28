class Circle:
  pi = 3.14

  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)


class SearchEngineEntry:
  secure_prefix = "https://"

  def __init__(self, url):
    self.url = url  # <--- here we are defining an instance variable and setting it

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"


class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    return self.score >= self.minimum_passing


gr = Grade(100)
pieter.add_grade(gr)
