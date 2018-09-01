"""
ID: s.sophi1
LANG: PYTHON3
PROG: sprime
"""

from math import sqrt
input = open('sprime.in', 'r')
output = open('sprime.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
input.close()


def is_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    return True


def is_super_prime(number):
    num_len = len(str(number))

    for i in range(num_len):
        if is_prime(number):
            number = number//10
        else:
            return False
    return True


def potential_super_primes(length, curr_num):
    if len(curr_num) == length:
        if is_super_prime(int(curr_num)):
            output.write(curr_num+'\n')
    else:
        first_num = ['2','3','5','7']
        not_first_num = ['1','3','7','9']
        if len(curr_num) == 0:
            for num in first_num:
                potential_super_primes(length, curr_num+num)
        else:
            for num in not_first_num:
                potential_super_primes(length, curr_num+num)


potential_super_primes(length, '')
output.close()
