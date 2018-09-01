"""
ID: s.sophi1
LANG: PYTHON2
PROG: dualpal
"""

input = open('dualpal.in', 'r')
output = open('dualpal.out', 'w')
string = input.readline().rstrip()
string = string.split()
needed_amount = int(string[0])
greater_than = int(string[1])
input.close()


def number_to_string(number, base):
    remainder = number % base
    quotient = number/base
    s = str(remainder)
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient/base
        s = str(remainder) + s
    return s


def is_palindrome(number_string):
    if number_string == number_string[::-1]:
        return True
    else:
        return False


def is_dual_palindrome(number):
    count = 0
    for base in range(2, 11):
        if is_palindrome(number_to_string(number, base)):
            count += 1
    if count >= 2:
        return True
    else:
        return False

counter = 0
i = 1
palindromes = []
while counter < needed_amount:
    if is_dual_palindrome(greater_than+i):
        counter += 1
        output.write(str(greater_than + i) + '\n')
    i += 1

output.close()