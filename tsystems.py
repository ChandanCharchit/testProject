class VectorMe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x+other.x, self.y+other.y

    def display(self):
        print(f'Vector after addition is {self.x}, {self.y}')

v1 = VectorMe(1, 2)
v2 = VectorMe(3, 4)
v1.display()
v2.display()
v3 = v1+v2
print(v3)

# a = Vector(1, 2)
# b = Vector(3, 4)
# print(a+b)           # Vector(4, 6)

