#main-0.py 
'''
# This code demonstrates polymorphism in Python using a base class and derived classes.
# It defines a base class `Shape` with an `area` method, and two derived classes `Rectangle` and `Circle`       
# that implement the `area` method in their own way.
# This allows us to call the `area` method on any `Shape` object, regardless of its specific type.
# polymorphism_demo.py
'''
class Shape: # This is the base class for all shapes.
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")# This ensures that any subclass of Shape must implement the area method.
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 
    def area(self):
        """This imports the math module to use the constant π (pi) for calculating the area of a circle.
        The area method calculates the area of the circle using the formula πr²."""
        import math #   
        return math.pi * (self.radius ** 2) # This calculates the area of a circle using the formula πr².
