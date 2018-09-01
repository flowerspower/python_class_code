"""
ID: s.sophi1
LANG: PYTHON2
PROG: crypt1
"""

input = open('crypt1.in', 'r')
output = open('crypt1.out', 'w')
strings = input.readlines()
strings = [x.rstrip() for x in strings]
num_count = int(strings[0])
numbers = [int(s) for s in strings[1].split()]
numbers = numbers[:num_count]
input.close()


def check_if_good(number):
    for c in str(number):
        n = int(str(c))
        if n not in numbers:
            return False
    return True


def check_possibility(number1, number2):
    number21 = int(str(number2)[0])
    number22 = int(str(number2)[1])
    mult1 = number22 * number1
    mult2 = number21 * number1
    if len(str(mult1)) == 3 and len(str(mult2)) == 3:
        if check_if_good(mult1) and check_if_good(mult2):
            if check_if_good(number1 * number2):
                return True
    return False


count = 0
for i in range(100, 1000):
    if check_if_good(i):
        for j in range(10, 100):
            if check_if_good(j):
                if check_possibility(i, j):
                    count += 1

output.write(str(count) + '\n')
output.close()
