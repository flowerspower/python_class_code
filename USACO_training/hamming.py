"""
ID: s.sophi1
LANG: PYTHON3
PROG: hamming
"""
input = open('hamming.in', 'r')
output = open('hamming.out', 'w')
N, B, D = input.readline().split()
input.close()


def hamming_distance(number1, number2):
    distance = 0
    binary1 = bin(number1)[2:]
    binary2 = bin(number2)[2:]
    max_len = max(len(binary1), len(binary2))
    zeros1 = ''
    zeros2 = ''

    for i in range(max_len-(len(binary1))):
        zeros1 += '0'
    for i in range(max_len-(len(binary2))):
        zeros2 += '0'

    binary1 = zeros1 + binary1
    binary2 = zeros2 + binary2

    for i in range(max_len):
        if binary1[i] != binary2[i]:
            distance += 1
    return distance


print(hamming_distance(25, 42))
print(N, B, D)
output.close()
