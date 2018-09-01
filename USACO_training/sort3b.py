"""
ID: s.sophi1
LANG: PYTHON3
PROG: sort3
"""
from collections import defaultdict
import heapq
import copy

input = open('sort3.in', 'r')
output = open('sort3.out', 'w')
lines = input.readlines()
input.close()

input_list = [int(string.strip()) for string in lines[1:]]
N = int(lines[0].rstrip())
sorted_list = sorted(input_list)

position_dict = defaultdict(list)
for index, elem in enumerate(input_list):
    position_dict[elem].append(index)


def mismatch_count(given_list, sorted_list):
    mismatches = 0
    for i in range(N):
        if given_list[i] != sorted_list[i]:
            mismatches += 1

    return mismatches


def exchange_canidates(given_list, sorted_list):
    position_dict = defaultdict(list)
    for index, elem in enumerate(given_list):
        position_dict[elem].append(index)

    exchanges = []
    for i in range(N):
        this_index_exchanges = []
        have_two = False
        what_it_is = given_list[i]
        what_it_should_be = sorted_list[i]
        if what_it_is != what_it_should_be:
            where_things_are = position_dict[what_it_should_be]
            for index in where_things_are:
                if given_list[index] != sorted_list[index]:
                    if sorted_list[index] == what_it_is:
                        this_index_exchanges.append((i, index, 2))
                        return [(i, index, 2)]
                        have_two = True
                        break
                    elif have_two == False:
                        this_index_exchanges.append((i, index, 1))
        if have_two:
            this_index_exchanges =[[a for a in this_index_exchanges if a[2] == 2][0]]
        exchanges += this_index_exchanges

    return exchanges


def apply_exchange(exchange, curr_list):
    updated_list = copy.deepcopy(curr_list)

    first = updated_list[exchange[0]]
    second = updated_list[exchange[1]]

    updated_list[exchange[0]] = second
    updated_list[exchange[1]] = first

    return updated_list


def is_in_pq(state, q):
    for t in q:
        if t[1] == state:
            return t
    return None


def heuristics(num_list):
    return mismatch_count(num_list, sorted_list)//2 + 1


def a_star_search(input_list):
    frontier = [(heuristics(input_list), input_list, 0)]
    heapq.heapify(frontier)
    explored = set([])

    while (frontier):
        node = heapq.heappop(frontier)

        if node[1] == sorted_list:
            return node[2]

        explored.add(tuple(node[1]))

        for exchange in exchange_canidates(node[1], sorted_list):
            updated_list = apply_exchange(exchange, node[1])
            child_cost = node[0]+1 + heuristics(updated_list)

            if tuple(updated_list) not in explored:
                heapq.heappush(frontier, (child_cost, updated_list, node[2]+1))
            else:
                thing = is_in_pq(updated_list, frontier)
                if thing and thing[0] > child_cost:
                    frontier.remove(thing)
                    frontier.append((child_cost, updated_list, node[2]+1))
                    heapq.heapify(frontier)

    return 'oops, no solution found'


def is_in_pq(state, q):
    for t in q:
        if t[1] == state:
            return t
    return None


def uniform_cost_search(input_list):
    frontier = [(0, input_list)]
    heapq.heapify(frontier)
    explored = set([])

    while (frontier):
        node = heapq.heappop(frontier)

        if node[1] == sorted_list:
            return node[0]

        explored.add(tuple(node[1]))

        for exchange in exchange_canidates(node[1], sorted_list):
            updated_list = apply_exchange(exchange, node[1])

            if tuple(updated_list) not in explored:
                heapq.heappush(frontier, (node[0]+1, updated_list))
            else:
                thing = is_in_pq(updated_list, frontier)
                if thing and thing[0] > node[0]+1:
                    frontier.remove(thing)
                    frontier.append((node[0]+1, updated_list))
                    heapq.heapify(frontier)

    return 'oops, no solution found'


print(exchange_canidates(input_list, sorted_list))
output.write(str(uniform_cost_search(input_list))+'\n')
output.close()
