easy version(mine)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
l = (''.join(random.sample(letters, nr_letters)))
print(l)
nr_symbols = int(input(f"How many symbols would you like?\n"))
n = (''.join(random.sample(symbols, nr_symbols)))
print(n)
nr_numbers = int(input(f"How many numbers would you like?\n"))
s = (''.join(random.sample(numbers, nr_numbers)))
print(s)


lns = [l, n, s]
print(lns)
random.shuffle(lns)
print(lns)

password=""
for pw in lns:
  password += pw
print(f"Password is : {password}")



or




hard version(angela)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw = []
for answer in range(1, nr_letters + 1):
  pw += random.choice(letters)

for answer in range(1, nr_symbols + 1):
  pw += random.choice(symbols)

for answer in range(1, nr_numbers + 1):
  pw += random.choice(numbers)
  
print(pw)

random.shuffle(pw)
print(pw)

password = ""
for answer in pw:
  password += answer

print(f"Password is: {password}")
