"""
ID: s.sophi1
LANG: PYTHON3
PROG: pprime
"""

input = open('pprime.in', 'r')
output = open('pprime.out', 'w')
string = input.readline().rstrip().split()
minimum = int(string[0])
maximum = int(string[1])
input.close()


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


def is_prime(number):
    for i in range(2, int(number/2)):
        if number % i == 0:
            return False
    return True


for i in range(minimum, maximum+1):
    if is_palindrome(i):
        if is_prime(i):
            print(i)

output.close()
