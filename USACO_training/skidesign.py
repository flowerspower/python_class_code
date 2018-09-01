"""
ID: s.sophi1
LANG: PYTHON3
PROG: skidesign
"""

input = open('skidesign.in', 'r')
output = open('skidesign.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
hill_heights = strings[1:]
hill_heights = [int(height) for height in hill_heights]
input.close()


def make_lines(heights, minnie_mouse, mickey_mouse):
    cost = 0
    for height in heights:
        if height > mickey_mouse:
            cost += (height-mickey_mouse)**2
        elif height < minnie_mouse:
            cost += (minnie_mouse-height)**2
    return cost


max_height = max(hill_heights)
min_height = min(hill_heights)
min_cost = 999999999999999999999999999999999999999999999999999999999999999999
if max_height-min_height <= 17:
    min_cost = 0
else:
    for i in range(17, max_height):
        min_height = max_height-17
        print(min_height, max_height)
        t = make_lines(hill_heights, min_height, max_height)
        max_height -= 1
        if t < min_cost:
            min_cost = t


output.write(str(min_cost)+'\n')
output.close()
