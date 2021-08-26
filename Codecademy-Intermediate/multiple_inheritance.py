class Employee():
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))


class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below


class Admin(Employee, User):
  def __init__(self):
    super().__init__() # calls Employee constructer since its listed first in line 24
    User.__init__(self, self.id, "Admin")  # need to pass 'self' to the Class.method call in this case

  def say_id(self):
    super().say_id()
    print("I am an admin.")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
