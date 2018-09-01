"""
ID: s.sophi1
LANG: PYTHON2
PROG: transform
"""
import copy

input = open('transform.in', 'r')
output = open('transform.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
matrix_size = int(strings[0])
original_matrix = []
transformed_matrix = []
input.close()

for i in range(matrix_size):
    original_matrix.append(list(strings[i+1]))
    transformed_matrix.append(list(strings[i+matrix_size+1]))


def print_matrix(matrix):
    for row in matrix:
        print(row)


def rotate_90(matrix):
    new_matrix = copy.deepcopy(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            new_matrix[j][(matrix_size-1)-i] = matrix[i][j]
    return new_matrix


def rotate_180(matrix):
    return rotate_90(rotate_90(matrix))


def rotate_270(matrix):
    return rotate_180(rotate_90(matrix))


def reflection(matrix):
    new_matrix = copy.deepcopy(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            new_matrix[i][matrix_size-j-1] = matrix[i][j]
    return new_matrix


if transformed_matrix == rotate_90(original_matrix):
    output.write('1\n')
elif transformed_matrix == rotate_180(original_matrix):
    output.write('2\n')
elif transformed_matrix == rotate_270(original_matrix):
    output.write('3\n')
elif transformed_matrix == reflection(original_matrix):
    output.write('4\n')
elif transformed_matrix == rotate_90(reflection(original_matrix)) or transformed_matrix == rotate_180(reflection(original_matrix) or transformed_matrix == rotate_270(reflection(original_matrix))):
    output.write('5\n')
elif transformed_matrix == original_matrix:
    output.write('6\n')
else:
    output.write('7\n')

output.close()
