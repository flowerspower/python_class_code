"""
ID: s.sophi1
LANG: PYTHON3
PROG: milk3
"""
from collections import deque
from copy import deepcopy

input = open('milk3.in', 'r')
output = open('milk3.out', 'w')
string = input.readline().rstrip()
string = string.split()
string = [int(x) for x in string]
input.close()


def pour(pour_out, pour_in, pour_cap):
    if pour_cap - pour_in - pour_out < 0:
        out = pour_out - (pour_cap - pour_in)
        inn = pour_cap
    else:
        out = 0
        inn = pour_out+pour_in
    return out, inn


def milkymilk(initial_milk, capacities):
    frontier = deque([initial_milk])
    explored = set([])
    solutions = set([])

    while (frontier):
        current_node = frontier.pop()
        current_state = current_node
        explored.add(tuple(current_state))
        for i in range(3):
            for j in range(3):
                if i != j:
                    results = pour(current_state[i], current_state[j], capacities[j])
                    child_state = deepcopy(current_state)
                    child_state[i] = results[0]
                    child_state[j] = results[1]

                    if child_state[0] == 0:
                        solutions.add(child_state[2])
                    if tuple(child_state) not in explored:
                        frontier.append(child_state)

    return sorted(solutions)


thing = [str(x) for x in milkymilk([0, 0, string[2]], string)]
output.write(" ".join(thing)+'\n')
output.close()
