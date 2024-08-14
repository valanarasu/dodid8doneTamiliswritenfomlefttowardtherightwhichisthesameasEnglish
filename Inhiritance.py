class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
  def printmy_name():
    print('Valan Arasu')  
  def myfunc():
    x = "awesome"
  x = "fantastic"
  print("Python is " + x)
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
Person.printmy_name()
Person.myfunc()