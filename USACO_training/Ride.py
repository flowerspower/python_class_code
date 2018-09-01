"""
ID: s.sophi1
LANG: PYTHON2
PROG: ride
"""

input = open('ride.in', 'r')
output = open('ride.out', 'w')
strings = input.readlines()
line1 = strings[0]
line2 = strings[1]
list1 = []
list2 = []

for letter in [l.strip() for l in line1.strip()]:
    x = ord(letter) - 64
    list1.append(x)

for letter in [l.strip() for l in line2.strip()]:
    x = ord(letter) - 64
    list2.append(x)

product1 = 1
product2 = 1

for number in list1:
    product1 = product1*number

for number in list2:
    product2 = product2*number

if product1 % 47 == product2 % 47:
    output.write("GO" + '\n')
else:
    output.write("STAY" + '\n')

output.close()
