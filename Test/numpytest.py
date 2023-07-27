# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# # An input string is valid if:
# # Open brackets are closed by the same type of brackets.
# # Open brackets are closed in the correct order.
# # Every close bracket has a corresponding open bracket of the same type.
# #
# # Example 1:
# # Input: s = "({})"
# # Output: true
# # Example 2:
# # Input: s = "()[]{}"
# # Output: true
# # Example 3:
# # Input: s = "(]"
# # Output: false
# # "}[{]"
#
#
# def correct_bracket(brackets):
#
#     b_dict = {']':'[', '}': '{', ')':'('}
#     b_stack = []
#
#     for item in brackets:
#         if item in b_dict.values():
#             b_stack.append(item)
#         elif item in b_dict.keys():
#             if not b_stack or (b_stack.pop() != b_dict[item]):
#                 return False
#
#     if not b_stack:
#         return True
#     else:
#         return False
#
#
# s = "{{{}}"
# print(correct_bracket(s))


# x = filter(lambda x: x%2, range(10))
#
# print(list(x))
# for i in x:
#     print(i)
# print(list(x))

l1 = [[1, 2, 3], [1, 2]]
l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
l2[1] = 10
# print(l1)
# print(l3)

t = (1, 2)
print(id(t))
t2=t
print(t2, id(t2))
t = t + (3,)

print(t)
print(id(t))
print(t2, id(t2))




