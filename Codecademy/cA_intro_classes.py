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
