# Method overriding
class Coffee:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def get_coffee(self):
        print("This is {} Coffee".format(self.coffee_type))


class MochaCoffee(Coffee):
    def __init__(self, coffee_type, sugar):
        self.sugar = sugar
        Coffee.__init__(self, coffee_type)

    def get_coffee(self):
        print("This is {} Coffee with {} sugar.".format(self.coffee_type, self.sugar))


c1 = Coffee("Latte")
c2 = MochaCoffee("Dologna", "Zero")

c1.get_coffee()
c2.get_coffee()


# Method Overloading

class ChocolateShake:
    def get_shake(self, dark, sugar, milk="1 large cup"):
        print("The shake was made by mixing {} chocolate, {} and {}".format(dark, sugar, milk))


thick_shake = ChocolateShake()

thick_shake.get_shake("55%", "2 tbsp")
thick_shake.get_shake("55%", "2 tbsp", "2 large cups")


# Operator overloading

class Mix:
    def __init__(self, coffee_shake, milk):
        self.coffee_shake = coffee_shake
        self.milk = milk

    def __add__(self, other):
        return Mix(self.coffee_shake+other.coffee_shake, self.milk+other.milk)

    def display(self):
        print("Coffee shake is made with {} beans and {} cups of milk.".format(self.coffee_shake, self.milk))


mix1 = Mix(3, 1)
mix2 = Mix(2, 2)

mix3 = mix1 + mix2
mix3.display()





