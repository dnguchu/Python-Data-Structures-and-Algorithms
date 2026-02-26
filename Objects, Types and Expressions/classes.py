"""
To create an instance of a class, a variable must be assigned to the class
The functions inside the class are called instance methods 
"""
#Problem 1
class Employee(object):
    numEmployee = 0 #used to count the number of employees created
    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)
    
    def pay(self):
        self.owed = 0
        return ("payed %s " %self.name)

emp1 = Employee('Dennis', 18.30)
emp2 = Employee('Toye', 20.50)

Employee.numEmployee

emp1.hours(20)
 
emp1.owed

emp1.pay()

#Problem 2
"""
Methods that start and end with double underscores are called special methods
The __init__ method is a special method that is invoked when an instance of the class is created
We can also implement custom special methods in custom objects
The __repr__ method is a special method that is used to return a string representation of the object
This is useful for inspecting or debugging and for displaying the object in a readable format
"""
class my_class():
    def __init__(self, greet):
        self.greet = greet
    def __repr__(self):
        return 'A custom object (%r)' %self.greet 
    
a = my_class('Hello')
a