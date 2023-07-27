from abc import ABC, abstractmethod


class Circle(ABC):
    def __init__(self, r=0):
        self.radius = r
        self.pi = 3.142

    @abstractmethod
    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius


class Sphere(Circle):
    Circle.area()



circle = Circle(5)
print("Area: {:.2f}".format(circle.area()))
print("Perimeter: {:.2f}".format(circle.perimeter()))
