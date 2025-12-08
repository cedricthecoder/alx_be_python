import math

class Shape:
    """Base class for different shapes."""
    
    def area(self):
        """Raises NotImplementedError to ensure derived classes override this method."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Rectangle class, inherits from Shape."""
    
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Override area method to calculate area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle class, inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius
    
    def area(self):
        """Override area method to calculate area of a circle."""
        return math.pi * (self.radius ** 2)
