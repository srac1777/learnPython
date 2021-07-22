def poem_description(date, autor, tile, work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
      publishing_date=date, author=autor, title=tile, original_work=work)
  return poem_desc


my_beard_description = poem_description(
    "1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
print(my_beard_description)

