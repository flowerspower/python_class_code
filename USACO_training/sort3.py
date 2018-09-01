"""
ID: s.sophi1
LANG: PYTHON3
PROG: sort3
"""

from collections import defaultdict
from collections import deque
import copy
import time

def mismatch_count(given_list, sorted_list):
    mismatches = 0
    for i in range(N):
        if given_list[i] != sorted_list[i]:
            mismatches += 1
        return mismatches


def exchange_candidates(given_list, sorted_list):
    position_dict = defaultdict(list)
    for index, elem in enumerate(given_list):
        position_dict[elem].append(index)

    exchanges = []
    for i in range(N):
        what_it_is = given_list[i]
        what_it_should_be = sorted_list[i]
        if what_it_is != what_it_should_be:
            where_things_are = position_dict[what_it_should_be]
            for index in where_things_are:
                if given_list[index] != sorted_list[index]:
                    if sorted_list[index] == what_it_is:
                        return [(i, index, 2)]
                    else:
                        exchanges.append((i, index, 1))

    return sorted(exchanges, key=lambda x : x[2], reverse=True)


def apply_exchange(exchange, curr_list):
    updated_list = copy.deepcopy(curr_list)

    first = updated_list[exchange[0]]
    second = updated_list[exchange[1]]

    updated_list[exchange[0]] = second
    updated_list[exchange[1]] = first

    return updated_list


def bfs_exchange(input_list):
    frontier = deque([(input_list, 0)])
    explored = set([])

    while frontier:
        current_state = frontier.popleft()

        if current_state[0] == sorted_list:
            return current_state[1]

        explored.add(tuple(current_state[0]))

        for exchange in exchange_candidates(current_state[0], sorted_list):
            updated_list = apply_exchange(exchange, current_state[0])

            if tuple(updated_list) not in explored:
                frontier.append((updated_list, current_state[1]+1))

    return 'oops, no solution found'


start = time.time()

input = open('sort3.in', 'r')
output = open('sort3.out', 'w')
lines = input.readlines()
input.close()

input_list = [int(string.strip()) for string in lines[1:]]
N = int(lines[0].rstrip())
sorted_list = sorted(input_list)

possible_exchanges = exchange_candidates(input_list, sorted_list)
position_dict = defaultdict(list)

for index, elem in enumerate(input_list):
    position_dict[elem].append(index)

output.write(str(bfs_exchange(input_list))+'\n')
output.close()

end = time.time()
print(end-start)
