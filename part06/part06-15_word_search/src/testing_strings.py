import re
word = ["care"]
x = ".a.e"
# p = x.count('.')
# before = x[:p]
# after = x[p+1:]
# print(p)

for i in word:
    if re.search(x, i):
        print(i)
