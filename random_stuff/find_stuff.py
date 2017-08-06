import random

p = random.randint(0,10)

carrots = []

for i in range(10):
    if p == i:
        carrots.append('purple carrot')
    else:
        carrots.append('orange carrot')

print carrots

def find_purple_carrot(carrots):
    for i in range(len(carrots)):
        if carrots[i] == 'purple carrot':
            return i

print find_purple_carrot(carrots)
