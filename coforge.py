
words = ['ab', 'yu', 'io']
line = "I am in Pune and I work daily."

words = line.split()
print(words)
unique_words = dict()
for word in words:
    if word not in unique_words:
        unique_words[word] = 1
    else:
        unique_words[word] += 1

print(unique_words)
for k, v in unique_words.



#
# def open_files(ftext):
#     with open(ftext, 'r') as f:
#          lines = f.readlines()
#          count = 0
#          for line in lines:





