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


# operator overloading
class Employee():
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1


class Meeting:
  def __init__(self):
    self.attendees = []

  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self): #overloading the len(obj) fn
    return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))
