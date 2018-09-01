"""
ID: s.sophi1
LANG: PYTHON3
PROG: wormhole
"""
from collections import deque

input = open('wormhole.in', 'r')
output = open('wormhole.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
wormhole_count = int(strings[0])
coordinates = strings[1:]
coordinates = [tuple([int(y) for y in x.split()]) for x in coordinates]
input.close()


def find_next_wormhole(exit_wormhole, wormholes):
    good_wormholes = []
    for wormhole in wormholes:
        if wormhole[1] == exit_wormhole[1] and wormhole[0] > exit_wormhole[0]:
            good_wormholes.append(wormhole)
    if len(good_wormholes) > 0:
        wormhole = sorted(good_wormholes)
        return wormhole[0]
    else:
        return None


def wormhole_one_hop(wormhole, pairings):
    for pair in pairings:
        if wormhole in pair:
            if pair[0] == wormhole:
                return pair[1]
            else:
                return pair[0]


def is_paring_looping(pairing):
    for wormhole_pair in pairing:
        for entering_wormhole in wormhole_pair:
            current_wormhole = entering_wormhole
            while current_wormhole:
                current_wormhole = wormhole_one_hop(current_wormhole, pairing)
                current_wormhole = find_next_wormhole(current_wormhole, coordinates)
                if current_wormhole == entering_wormhole:
                    return True
    return False


def find_all_parings(wormholes):
    wormhole_num = len(wormholes)
    queue = deque()

    for i in range(1, wormhole_num):
        queue.append([(wormholes[0], wormholes[i])])

    while len(queue[0]) < wormhole_num/2:
        first_pairing = queue.popleft()
        remaining_wormholes = sorted(set(wormholes)-set([item for w in first_pairing for item in w]))
        for i in range(1, len(remaining_wormholes)):
            queue.append(first_pairing + [(remaining_wormholes[0], remaining_wormholes[i])])

    return queue


counter = 0
for pairing in find_all_parings(coordinates):
    if is_paring_looping(pairing):
        counter +=1

output.write(str(counter)+'\n')
output.close()
