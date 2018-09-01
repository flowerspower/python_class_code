"""
ID: s.sophi1
LANG: PYTHON2
PROG: gift1
"""

input = open('gift1.in', 'r')
output = open('gift1.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
current_line_number = 0


def read_number(line):
    return int(strings[line])


def read_name(names, name):
    for i in range(len(names)):
        if name == names[i]:
            return name

amount_of_people = read_number(0)
people = strings[1:amount_of_people+1]
current_line_number += amount_of_people
accounts = {}
for person in people:
    accounts[person] = 0


def update_accounts(accounts, giver, receivers, num_receivers, amount):
    accounts[giver] -= amount
    for receiver in receivers:
        accounts[receiver] += amount/num_receivers
    accounts[giver] += amount % num_receivers


while current_line_number+1 < len(strings):
    print current_line_number + 1
    giver = strings[current_line_number + 1]
    current_line_number += 1
    money_giving = int(strings[current_line_number + 1].split()[0])
    people_receiving_num = int(strings[current_line_number + 1].split()[1])
    current_line_number += 1
    people_getting = strings[current_line_number+1:current_line_number+people_receiving_num+1]
    current_line_number += people_receiving_num

    if money_giving != 0:
        update_accounts(accounts, giver, people_getting, people_receiving_num, money_giving)

for person in people:
    output.write(person + ' ' + str(accounts[person]) + '\n')

output.close()
