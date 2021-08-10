def painting(paint_colors, picture):
  painting_statement = "To paint the " + \
      picture + " we need the following colors: "
  print(painting_statement)
  for color in paint_colors:
      print(color)


painting(['Orange', 'White', 'Green'], 'Indian Flag')


def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!

  def calc_gallons():
    return square_feet / 400
  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30, 20)))


def enclosing_function():
  var = "value"

  def nested_function():
    nonlocal var
    var = "new_value"

  nested_function()
  print(var)


enclosing_function()
