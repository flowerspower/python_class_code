import random

random_numbers = []
even_numbers = []
odd_numbers = []

for i in range(10):
    x = random.randint(1,100)
    random_numbers.append(x)
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print random_numbers
print even_numbers
print odd_numbers