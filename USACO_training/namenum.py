"""
ID: s.sophi1
LANG: PYTHON2
PROG: namenum
"""

input = open('namenum.in', 'r')
input_2 = open('dict.txt', 'r')
output = open('namenum.out', 'w')
strings = input.readlines()
dict_strings = input_2.readlines()
number_code = strings[0].rstrip()
valid_names = [line.rstrip() for line in dict_strings]
input.close()
input_2.close()
letters_to_numbers = {}
names_as_codes = {}
codes_as_names = {}

numbers_to_letters = {
    2: ('A', 'B', 'C'),
    3: ('D', 'E', 'F'),
    4: ('G', 'H', 'I'),
    5: ('J', 'K', 'L'),
    6: ('M', 'N', 'O'),
    7: ('P', 'R', 'S'),
    8: ('T', 'U', 'V'),
    9: ('W', 'X', 'Y')
}


def name_to_code(name):
    code = ''
    for letter in name:
        if letters_to_numbers.get(letter) == None:
            return None
        code += str(letters_to_numbers[letter])
    return code


for number in numbers_to_letters:
    for letter in numbers_to_letters[number]:
        letters_to_numbers[letter] = number

for name in valid_names:
    if name_to_code(name) != None:
        names_as_codes[name] = name_to_code(name)

for name in names_as_codes:
    code = name_to_code(name)
    if code not in codes_as_names:
        codes_as_names[code] = [name]
    else:
        codes_as_names[code].append(name)

if number_code not in codes_as_names:
    output.write('NONE\n')
else:
    output.write('\n'.join(sorted(codes_as_names[number_code])) + '\n')

output.close()
