# f(n) = f(n - 1) + f(n - 2) + f(n - 3)
# for n>= 3
#
# where
# f(0) = 0, f(1) = 1 and f(2) = 2
# determine
# f(x)

# def recursive_f(n):
#     result = 0
#     if n < 3:
#         return n
#     else:
#         for i in range(3, n, 1):
#             result += recursive_f(i)
#             return result
#             # return recursive_f(n-1) + recursive_f(n-2) + recursive_f(n-3)
#
#
# result = recursive_f(7)
# print(result)




hello = {'Text': ['Hello world', 'Python is awesome', 'Hello again']}

vocab = ''
for item in hello['Text']:
    vocab += item
    print(vocab)
stack = {}

for item in vocab.split():
    if item not in stack:
        stack[item] = 1
    else:
        stack[item] += 1

print(stack)













