tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Write your code below: 
def assign_table(table_number, name, vip_status = False):
  tables[table_number] = [name, vip_status]

assign_table(6, "Yoni", False)


assign_table(name="Martha", table_number=3, vip_status=True)

assign_table(4, "Karla")

print(tables)



tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Write your code below: 
def assign_and_print_order(table_number, *order_items):
  # pass
  tables[table_number]['order'] = order_items
  for item in order_items:
    print(item)

assign_table(2, "Arwa", True)
assign_and_print_order(2, "Steak", "Seabass", "Wine Bottle")

print(tables)


tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


# Write your code below: 
def assign_food_items(**order_items):
   print(order_items)
   food = order_items.get("food")
   drinks = order_items.get("drinks")
   print(food)
   print(drinks)
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')