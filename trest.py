# => [1, 2, 4, 3]
#
# target = 4
# return pair exists or no (bool)
def to_lowercase(func):
    def wrapper(*args, **kwargs):
        args = [str(arg).lower() for arg in args]
        kwargs = {k: str(v).lower() for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper


# def to_lowercase(func):
#     def wrapper(name):
#         name = name.lower()
#         return func(name)
#     return wrapper

@to_lowercase
def greet(name):
    print(f"Hello, {name}!")


print(greet('Anuj'))

# emp_name         emp_salary
#
# Shubham Thakur  50000.00
# Aman Chopra     60000.50
# Naveen Tulasi   75000.75
# Bhavika uppala  45000.25
# Nishant jain    80000.00
# Max salary emp






