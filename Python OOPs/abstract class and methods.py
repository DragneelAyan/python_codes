#By default, Python does not provide abstract classes. The ‘abc’ module in the Python library 
#provides the infrastructure for defining custom abstract base classes.
from abc import ABC, abstractmethod

#Abstract class is a class which has abstract method. 
class Shape(ABC): #This is a abstract class.
    @abstractmethod #Abstract method
    def printarea(self):
        return 0
# This Shape abstract class is like a unwritten rule which gets imposed when one normal class inherits it. 
#Here the rule is that every child class of Shape class must have the abstract method 'def printarea()'    

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def printarea(self):
        return(self.length**2)
#This class has the 'printarea' method, so it runs smoothly        
        
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def printdiameter(self):
        return(2*self.length + 2*self.breadth)
# [TypeError: Can't instantiate abstract class Rectangle with abstract method printarea]
# This Rectangle class doesn't have 'printarea' method in it, so it shows error.         

shape1 = Square(6)
print(shape1.printarea())

shape2 = Rectangle(4,7)
print(shape2.printarea())

       
                