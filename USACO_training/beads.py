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


def beads_collected(beads, cut):
    len_beads = len(beads)
    right_bead = beads[cut]
    left_bead = beads[cut-1]
    right_pointer = cut
    left_pointer = cut-1
    right_collected = 0
    left_collected = 0
    left_wrapped_around = False

    while beads[left_pointer] in ['w', left_bead]:
        if beads[left_pointer] == 'w':
            left_collected += 1
            left_pointer -= 1
            if left_pointer < 0:
                left_wrapped_around = True
                left_pointer = len_beads + left_pointer
            if left_collected + right_collected >= len_beads:
                break
            if left_bead == 'w':
                left_bead = beads[left_pointer]
            continue

        left_collected += 1
        left_pointer -= 1
        if left_pointer < 0:
            left_wrapped_around = True
            left_pointer = len_beads + left_pointer
        if left_collected + right_collected >= len_beads:
            break

    while (beads[right_pointer] == right_bead or beads[right_pointer] == 'w') \
            and (not left_wrapped_around or (left_wrapped_around and right_pointer <= left_pointer)):
        if beads[right_pointer] == 'w':
            right_collected += 1
            right_pointer += 1
            right_pointer = right_pointer % len_beads
            if left_collected + right_collected >= len_beads:
                break
            if right_bead == 'w':
                right_bead = beads[right_pointer]
            continue
        right_collected += 1
        right_pointer += 1
        right_pointer = right_pointer % len_beads
        if left_collected + right_collected >= len_beads:
            break

    return min(left_collected + right_collected, len_beads)


def find_max_beads(beads_string):
    max_beads = 0
    for position in range(len(beads_string)):
        beads_collect = beads_collected(beads_string, position)
        if beads_collect > max_beads:
            max_beads = beads_collect
    return max_beads

# print find_max_beads('wwww') == 4
# print find_max_beads('rrwwwwbb') == 8
# print find_max_beads('bbwwwbb') == 7
# print find_max_beads('bbbrrr') == 6
# print beads_collected('wwwbbrwrbrbrrbrbrwrwwrbwrwrrb', 28)
# print find_max_beads('rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr')

output.write(str(find_max_beads(beads_string))+ '\n')
output.close()

# print find_max_beads('rrbbrbbbwbwwbwbbbbwwrrbbwbrwbrwbbbrbrwrwbrwwwrrbbrrwrbbrwbwrwwwrbrwwwwwrwbwwwrrbrrbbbrbrbbbrbbbrbbwbbbbbrbrrbrwwbrrrrwbwrwrbbwbwrbrbrwwbrrbwbrwwbwwwbrbwrwbwbrbbbwrbwwrrrbwbwbbbbbrrwwwrbrwwrbbwrbbrbbrbwrrwwbrrrbrwbrwwrbwbwrrrbwrwrrbrbbwrwrbrwwwrwbwrrwwwwrrrwrrwbbwrwwrwrbwwbwrrrrbbwrbbrbwwwwwbrbbrbbrbrwbbwbwwbbbbbwwwrbwwbbbwrwwbbrrwrwbwrrwwwrrrwrrwww')