# Length of longest consecutive ones by at most one swap in a Binary String
# I/P: 111011101
# O/P: 7
#
#
# def consecutive_one(input_one):
#     in_arr = input_one.split('0')
#     print(in_arr)
#     len_arry = []
#     for item in in_arr:
#         len_arry.append(len(item))
#     print(len_arry)
#     # length = len(input_one)
#     # for item in input_one:
# print(consecutive_one('1110110101'))
# input1 is array
# input is int
# I/P:- 1234567, 2
# O/P:- 6712345
# def rotate_str(num, rotation):
#     rotated_num = num
#     if (len(num)!=0) and rotation>=0:
#         i = rotation % len(num)
#         rotated_num = num[-i:] + num[:-i]
#
#     return rotated_num


#
# ar = '1234567'
# arr = [i for i in ar]
# # print(arr)
# print(rotate_str(arr, -2))
class Wow:
    def compute(self, s, t, sb = None, start_idx=0, next_start=0):
        if len(t) > len(s):
            return ''
        if sb is None:
            sb = []
        pattern = t
        stack = [i for i in t]
        max_len = len(stack)
        if max_len == 1 and (t not in s):
            return ''
        for idx, item in enumerate(s):
            if idx > len(s):
                break
            if item in stack:
                stack.remove(item)
                if len(stack) == max_len - 1:
                    start_idx = idx
                elif len(stack)== max_len - 2:
                    if len(stack)==0:
                        pass
                    else:
                        next_start = idx
                if len(stack) == 0:
                    end_idx = idx
                    stack = [j for j in pattern]
                    sb.append(s[start_idx:end_idx + 1])
                    print(sb)
                    if next_start:
                        s = s[next_start:]
                        self.compute(s, stack, sb)
        if sb:
            min_string = min(sb, key=len)
            return min_string
        else:
            pass


substring_list = []

w1 = Wow()
print(w1.compute('bba', 'ab', substring_list))



    # if sb:
    #     lb = [len(item) for item in sb]
    #     print('min length substring', min(lb))


# substring_list = []
# print(compute('ADOBECODEBANC', 'ABC', substring_list))
