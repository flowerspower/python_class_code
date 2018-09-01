"""
ID: s.sophi1
LANG: PYTHON2
PROG: beads
"""

input = open('beads.in', 'r')
output = open('beads.out', 'w')
lines = input.readlines()
input.close()

beads_count = int(lines[0].rstrip())
beads_string = lines[1].rstrip()[:beads_count]


def find_max_beads(beads_string):
    array_columns = len(beads_string) * 2
    len_beads = len(beads_string)
    beads_string = beads_string + beads_string
    left_r = [0 for i in range(array_columns)]
    left_b = [0 for i in range(array_columns)]
    for i in range(array_columns - 1):
        next_bead = beads_string[i]
        if next_bead == 'r':
            left_b[i+1] = 0
            left_r[i+1] = left_r[i]+1
        elif next_bead == 'b':
            left_b[i+1] = left_b[i]+1
            left_r[i+1] = 0
        else:
            left_b[i+1] = left_b[i]+1
            left_r[i+1] = left_r[i]+1

    right_r = [0 for i in range(array_columns)]
    right_b = [0 for i in range(array_columns)]
    next_bead = beads_string[-1]
    if next_bead == 'r':
        right_b[-1] = 0
        right_r[-1] = 1
    elif next_bead == 'b':
        right_b[-1] = 1
        right_r[-1] = 0
    else:
        right_b[-1] = 1
        right_r[-1] = 1

    for i in range(array_columns - 1, 0, -1):
        next_bead = beads_string[i-1]
        if next_bead == 'r':
            right_b[i-1] = 0
            right_r[i-1] = right_r[i]+1
        elif next_bead == 'b':
            right_b[i-1] = right_b[i]+1
            right_r[i-1] = 0
        else:
            right_b[i-1] = right_b[i]+1
            right_r[i-1] = right_r[i]+1

    max_right = [0 for i in range(array_columns)]
    max_left = [0 for i in range(array_columns)]
    max_overall = [0 for i in range(array_columns)]
    for i in range(array_columns):
        max_right[i] = max(right_b[i], right_r[i])
        max_left[i] = max(left_b[i], left_r[i])
        max_overall[i] = max_left[i] + max_right[i]
    return min(max(max_overall), len_beads)

output.write(str(find_max_beads(beads_string))+ '\n')
output.close()
