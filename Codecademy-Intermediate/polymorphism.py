class Employee():
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))


class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")


class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")


# Write your code below
e = Employee()
a = Admin()
m = Manager()
meeting = [e, a, m]

for user in meeting:
  user.say_id() # different objects having same behavior (no need to worry about which class it belongs to)
