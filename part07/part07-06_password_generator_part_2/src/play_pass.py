import random
import string

num = 8
all = string.printable.strip()
# print(all)
numbers = list(string.digits)
special = list(string.punctuation)
letters = list(string.ascii_letters)

print(numbers, special, letters)

password_list = []
for i in range(num):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# rint(password_list)

# print(random.shuffle(all))
# print(random.sample(all, 8))