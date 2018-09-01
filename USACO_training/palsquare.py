"""
ID: s.sophi1
LANG: PYTHON2
PROG: palsquare
"""

input = open('palsquare.in', 'r')
output = open('palsquare.out', 'w')
strings = input.readlines()
base_number = int(strings[0].rstrip())
input.close()


def convert_digit_to_letter(d):
    letters = 'ABCDEFGHIJKLMN'
    if d >= 10:
        return letters[d-10]
    else:
        return str(d)


def number_to_string(number, base):
    remainder = number % base
    quotient = number/base
    string = convert_digit_to_letter(remainder)
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient/base
        string = convert_digit_to_letter(remainder) + string
    return string


def is_palindrome(number_string):
    if number_string == number_string[::-1]:
        return True
    else:
        return False


for i in range(1, 301):
    if is_palindrome(number_to_string(i*i, base_number)):
        output.write(number_to_string(i, base_number) + ' ' + number_to_string(i*i, base_number) + '\n')

output.close()
