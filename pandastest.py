class Mix:
    def __init__(self, coffee, sugar):
        self.coffee = coffee
        self.sugar = sugar

    def __add__(self, other):
        return Mix(self.coffee+other.coffee, self.sugar+other.coffee)

    def display(self):
        print("coffee shake is made with {} coffee and {} sugar.".format(self.coffee, self.sugar))


mix1 = Mix(2, 6)
mix2 = Mix(2, 4)

mix3  = mix1+mix2

mix3.display()
