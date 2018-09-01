"""
ID: s.sophi1
LANG: PYTHON3
PROG: castle
"""
from collections import defaultdict

input = open('castle.in', 'r')
output = open('castle.out', 'w')
strings = [string.rstrip() for string in input.readlines()]
length, height = [int(string) for string in strings[0].split()]
castle = []
converted_castle = []
adjacency_matrix = defaultdict(list)

for i in range(1, height+1):
    castle.append([int(string) for string in strings[i].split()])
input.close()

for row in castle:
    binaries = []
    for num in row:
        binary = bin(num)[2:]
        while len(binary) < 4:
            binary = '0' + binary
        binaries.append(binary)
    converted_castle.append(binaries)

for i in range(height):
    for j in range(length):
        if converted_castle[i][j] == '1111':
            adjacency_matrix[(i, j)] = []
        if converted_castle[i][j][0] == '0':
            adjacency_matrix[(i,j)].append((i+1, j))
        if converted_castle[i][j][1] == '0':
            adjacency_matrix[(i,j)].append((i, j+1))
        if converted_castle[i][j][2] == '0':
            adjacency_matrix[(i,j)].append((i-1, j))
        if converted_castle[i][j][3] == '0':
            adjacency_matrix[(i,j)].append((i, j-1))

visited_nodes = set()


def get_connected_components(node):
    connected_components = set()
    nodes = [node]
    while nodes:
        node = nodes.pop()
        visited_nodes.add(node)
        connected_components.add(node)
        for neighbor in adjacency_matrix[node]:
            if neighbor not in visited_nodes:
                nodes.append(neighbor)
    return connected_components


def get_all_connected_components():
    all_connected_components = []
    for node in adjacency_matrix:
        if node not in visited_nodes:
            room = get_connected_components(node)
            all_connected_components.append(room)
    return all_connected_components


rooms = get_all_connected_components()
room_count = len(rooms)
room_sizes = []
for room in rooms:
    room_sizes.append(len(room))

barney_the_dinoary = {} #square to room dict
for room_index in range(room_count):
    for s in rooms[room_index]:
        barney_the_dinoary[s]=room_index
print(barney_the_dinoary)

mergeable = defaultdict(list)

for i in range(height):
    for j in range(length):
        this_square = (i, j)
        east_square = (i+1, j)
        south_square = (i, j-1)
        this_room = barney_the_dinoary.get(this_square)
        east_room = barney_the_dinoary.get(east_square)
        south_room = barney_the_dinoary.get(south_square)
        if this_room != east_room and east_room != None:
            mergeable[len(rooms[this_room])\
                      +len(rooms[east_room])].append((this_square, east_square))
        if this_room != south_room and south_room != None:
            mergeable[len(rooms[this_room])\
                      +len(rooms[south_room])].append((this_square, south_square))

largest_combined_room = max(dict(mergeable).keys())


def key_func(x):
    square_a = x[0]
    square_b = x[1]
    if square_a[1] < square_b[1]:
        square = (square_a, 'E')
    elif square_b[1] < square_a[1]:
        square = (square_b, 'E')
    elif square_a[0] > square_b[0]:
        square = (square_a, 'N')
    elif square_b[0] > square_a[0]:
        square = (square_b, 'N')
    print(square)
    return (square[0][1], -square[0][0], -ord(square[1]))

print(largest_combined_room)
square_pair_candidates = mergeable[largest_combined_room]
print(square_pair_candidates)

info = sorted([key_func(x)for x in square_pair_candidates])[0]

# print(key_func(((2, 2), (3, 2))))
output.write(str(room_count)+'\n')
output.write(str(max(room_sizes))+'\n')
output.write(str(largest_combined_room)+'\n')
output.write(str((info[1]*-1)+1) + ' ' + str(info[0]+1) + ' ' + str(chr(info[2]*-1)) + '\n')
output.close()
