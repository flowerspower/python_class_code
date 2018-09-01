"""
ID: s.sophi1
LANG: PYTHON2
PROG: combo
"""

input = open('combo.in', 'r')
output = open('combo.out', 'w')
strings = [s.rstrip() for s in input.readlines()]
number_max = int(strings[0])
lock_combo = [int(s) for s in strings[1].split()]
master_combo = [int(s) for s in strings[2].split()]
input.close()


def good_positions(x, N):
    return [(N+x-3) % N+1, (N+x-2) % N+1, x, x % N+1, (x+1) % N+1]


def check_if_combo_works(combo):
    if combo[0] in good_positions(lock_combo[0], number_max) and \
        combo[1] in good_positions(lock_combo[1], number_max) and \
        combo[2] in good_positions(lock_combo[2], number_max):
        return True

    if combo[0] in good_positions(master_combo[0], number_max) and \
        combo[1] in good_positions(master_combo[1], number_max) and \
        combo[2] in good_positions(master_combo[2], number_max):
        return True
    return False


counter = []
for a in good_positions(lock_combo[0], number_max):
    for b in good_positions(lock_combo[1], number_max):
        for c in good_positions(lock_combo[2], number_max):
            if check_if_combo_works((a, b, c)):
                counter.append((a, b, c))

for d in good_positions(master_combo[0], number_max):
    for e in good_positions(master_combo[1], number_max):
        for f in good_positions(master_combo[2], number_max):
            if check_if_combo_works((d, e, f)):
                counter.append((d, e, f))

output.write(str(len(set(counter)))+'\n')
output.close()
