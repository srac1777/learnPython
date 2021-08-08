print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 
print(globals())


# Write Checkpoint 2 here: 

global_variable = 'global'


# Write Checkpoint 3 here: 

def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'


print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here: 



print(globals())



global_variable = 'global'



print(' -- Global Namespace with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

print(' \n -- Local Namespace with empty script -- \n')
# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1 / num2
  print(locals())

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())



print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3,4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4,50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())


global_variable = 'global'


global_variable = 'global'


def outer_function():
  outer_value = "outer"

  def inner_functon():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())

  inner_functon()


outer_function()
