"""
ID: s.sophi1
LANG: PYTHON3
PROG: numtri
"""

input = open('numtri.in', 'r')
output = open('numtri.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
triangle = [string.split() for string in strings[1:]]
input.close()

for list in triangle:
    counter = 0
    for string in list:
        list[counter] = int(string)
        counter += 1


def find_largest_sum(triangle):
    dp_table = [triangle[0]]
    for i in range(1, len(triangle)):
        dp_row =[0 for x in range(len(triangle[i]))]
        first_num = triangle[i][0]
        last_num = triangle[i][-1]
        dp_row[0] = first_num + dp_table[i-1][0]
        dp_row[-1] = last_num + dp_table[i-1][-1]
        dp_table.append(dp_row)

    for i in range(2, len(triangle)):
        for j in range(1, len(dp_table[i])-1):
            dp_table[i][j] = max(dp_table[i-1][j-1],dp_table[i-1][j]) + triangle[i][j]
    return max(dp_table[-1])


output.write(str(find_largest_sum(triangle)) + '\n')
output.close()
