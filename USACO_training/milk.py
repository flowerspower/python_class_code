"""
ID: s.sophi1
LANG: PYTHON2
PROG: milk
"""

input = open('milk.in', 'r')
output = open('milk.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
milk_wanted, farmer_count = strings[0].split()
strings = [string.split() for string in strings]
milk_wanted = int(milk_wanted)
farmer_count = int(farmer_count)
input.close()

farmer_dict = {}

for i in range(farmer_count):
    if int(strings[i+1][0]) not in farmer_dict:
        farmer_dict[int(strings[i+1][0])] = int(strings[i+1][1])
    else:
        farmer_dict[int(strings[i + 1][0])] += int(strings[i + 1][1])

costs = sorted(farmer_dict)
i = 0
cost = 0
while milk_wanted != 0:
    if farmer_dict[costs[i]] == 0:
        i += 1
    farmer_dict[costs[i]] -= 1
    cost += costs[i]
    milk_wanted -= 1

output.write(str(cost) + '\n')
output.close()
