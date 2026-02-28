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

#Problem 3
#Inheritance
"""
Inheritance allows us to create a new class that modifies the behavior of an existing class
This is achieved by passing the existing class as an argument to the new class
"""
class specialEmployee(Employee):
    """
    For a subclass to define new class variables, it needs to define an __init__ method as follows
    """
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate) #Calls the __init__ method of the base class
        self.bonus = bonus

    def hours(self, numHours):
        self.owed += numHours * self.rate * 2
        return ('%.2f hours worked' % numHours)

    """
    Methods of the base class are not automatically invoked and it is necessary for the 
    derived class to call them explicitly using the super() function or by calling the method of the base class directly
    """
    def pay(self):
        #self.owed = 0
        super().pay() #Calls the pay method of the base class and resets owed using base implementation
        return ('payed %s with a bonus of %s' %(self.name, self.bonus))
    
spemp = specialEmployee('Guchu', 18.30, 1000)
spemp.pay()

#Problem 4
"""
Within a class definition not all methods operate on the instance of the class
Static methods do not perform any operations on the class instance and is defined using the @staticmethod decorator
Class methods operate on the class itself and is defined using the @classmethod decorator
Class methods take the class as the first argument and is conventionally named cls
"""
class Aexp(object):
    base = 2
    @classmethod
    def exp(cls, x):
        return(cls.base ** x)
    
class Bexp(Aexp):
    base = 3

Bexp.exp(3)