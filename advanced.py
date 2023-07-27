def count_upto_n(n):
    x = 1
    while x <= n:
        yield x
        x += 1


# for number in count_upto_n(7):
#     print(number)


def to_uppercase(func):
    def wrapper(name):
        name = name.upper()
        return func(name)
    return wrapper


@to_uppercase
def company_name(name):
    print("I work at {}".format(name))


print(company_name('t systems'))


class CountUpTo:
    def __init__(self , n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count>self.n:
            raise StopIteration
        else:
            self.count += 1
            return self.count-1


c1 = CountUpTo
for number in c1(5):
    print(number)


