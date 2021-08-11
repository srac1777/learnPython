def add_two(my_input):
    return my_input + 2

add_three = lambda my_input: my_input + 3

pop = add_three(2)
print(pop)

#if statement lambdas
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

print(check_if_A_grade(90))

