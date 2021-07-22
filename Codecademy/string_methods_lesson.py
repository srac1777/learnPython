def poem_description(date, autor, tile, work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
      publishing_date=date, author=autor, title=tile, original_work=work)
  return poem_desc


my_beard_description = poem_description(
    "1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
print(my_beard_description)


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)
highlighted_poems_stripped = []

for l in highlighted_poems_list:
  highlighted_poems_stripped.append(l.strip())

print(highlighted_poems_stripped)
highlighted_poems_details = []

for m in highlighted_poems_stripped:
  highlighted_poems_details.append(m.split(":"))

titles = []
poets = []
dates = []

for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])

for i in range(len(titles)):
  print("The poem {title} was published by {poet} in {date}.".format(
      title=titles[i], date=dates[i], poet=poets[i]))
