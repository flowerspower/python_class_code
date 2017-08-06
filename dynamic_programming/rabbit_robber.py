# This program uses dynamic programming to solve the following
# problem:
# A bad rabbit goes through Manhattan to rob banks. The Manhattan
# in this story is basically a N x N grid, where there are horizontal
# and vertical streets. The rabbit enters the grid at the upper-left
# corner and exits at the lower-right corner. It is only allowed to
# go west or south along streets. There are banks and big bad wolves
# on some of the blocks. These wolves are stationary because they are
# too lazy to move. If the rabbit goes past a bank, it will rob
# the bank and get $10,000. If the rabbit goes past a wolf,
# it will be robbed by the wolf and lose $20,000. It is possible to rob
# a bank twice if the rabbit goes along the street to the north of it and
# the street to the east of it. It is also possible for the rabbit to rob
# two banks while going along the street between two blocks if both happen
# to have banks. Same thing for wolves. If the rabbit has $10,000 at hand
# and gets robbed by a wolf, it will end up with -$10,000, which means that
# it owes the wolf $10,000.
# The rabbit has no money initially. The goal of the rabbit is to find the
# best path possible that leads to the maximum amount of money when it exits
# Manhattan.
# A brute force algorithm will have to examine O(2^2N) possible paths, so it
# will take billions of years to run on the fastest computer to find the best
# solution for a grid that has a few hundred rows.
# The dynamic programming algorithm, however, can solve it in a couple of seconds,
# or even less than one second.

import numpy as np
import random

n_row = 100
n_col = 100
manhattan_grid = np.chararray((n_row, n_col))

banks = 500
wolves = 100
manhattan_grid[:] = 'O' # fill up manhattan_grid with 'O', which means empty block
rand_locations = set([])

while len(rand_locations) < banks+wolves:
    rand_locations.add((random.randint(0, n_row - 1), random.randint(0, n_col - 1)))

rand_locations = list(rand_locations)

for i in range(banks):
    manhattan_grid[rand_locations[i]] = 'B'

for i in range(banks, banks+wolves):
    manhattan_grid[rand_locations[i]] = 'W'

print 'The Manhattan blocks look like this:'
for i in range(n_row):
    for j in range(n_col):
        print manhattan_grid[i,j],
    print

dp_table = np.zeros(shape=(n_row+1,n_col+1))

# table that stores the choices made by the rabbit at each intersection
choices_table = np.chararray(shape=(n_row+1,n_col+1))
choices_table[0, 0] = 'O'

def get_block_entity(r, c):
    if r >= 0 and r < n_row and c >= 0 and c < n_col:
        return manhattan_grid[r,c]
    else:
        return None


# When the rabbit tries to figure out the best way to go to
# the intersection at r row and c column, it needs to know
# what kinds of entities lie long the streets.
# This function finds the entities in the NW, NE and SW blocks
# and returns them in a tuple (NW entity, NE entity, SW entity)
def find_entities(r, c):
    nw_block_entity = get_block_entity(r - 1, c - 1)
    ne_block_entity = get_block_entity(r - 1, c)
    sw_block_entity = get_block_entity(r, c - 1)
    return (nw_block_entity, ne_block_entity, sw_block_entity)


# filling up the first row of dp_table
for c in range(1, n_col+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(0, c)
    if sw_block_entity == 'B':
        dp_table[0,c] = dp_table[0,c-1] + 10000
    elif sw_block_entity == 'W':
        dp_table[0,c] = dp_table[0,c-1] - 20000
    else:
        dp_table[0,c] = dp_table[0,c-1]
    choices_table[0, c] = 'W'

# filling up the first column of dp_table
for r in range(1, n_row+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, 0)
    if ne_block_entity == 'B':
        dp_table[r,0] = dp_table[r-1,0] + 10000
    elif ne_block_entity == 'W':
        dp_table[r,0] = dp_table[r-1,0] - 20000
    else:
        dp_table[r,0] = dp_table[r-1,0]
    choices_table[r, 0] = 'N'

for r in range(1, n_row+1):
    for c in range(1, n_col+1):
        (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, c)
        # find money stored at intersection above
        north_intersection_money = dp_table[r-1][c]
        option1_money = north_intersection_money
        if nw_block_entity == 'B':
            option1_money += 10000
        if nw_block_entity == 'W':
            option1_money -= 20000
        if ne_block_entity == 'B':
            option1_money += 10000
        if ne_block_entity == 'W':
            option1_money -= 20000
        # find money stored at intersection to the left
        west_intersection_money = dp_table[r,c-1]
        option2_money = west_intersection_money
        if nw_block_entity == 'B':
            option2_money += 10000
        if nw_block_entity == 'W':
            option2_money -= 20000
        if sw_block_entity == 'B':
            option2_money += 10000
        if sw_block_entity == 'W':
            option2_money -= 20000

        if option1_money > option2_money:
            dp_table[r, c] = option1_money
            choices_table[r, c] = 'N'
        else:
            dp_table[r, c] = option2_money
            choices_table[r, c] = 'W'

print 'The complete dynamic programming table is:'
print np.array_str(dp_table, max_line_width = 1000000)

print 'The largest amount of money the rabbit can possibly have when exiting Manhattan is $%d' % (dp_table[n_row,n_col])

print choices_table

best_path = []
this_choice = choices_table[n_row, n_col]
r = n_row
c = n_col

while this_choice != 'O':
    if this_choice == 'W':
        best_path.append('E')
        c -= 1
        this_choice = choices_table[r, c]
    if this_choice == 'N':
        best_path.append('S')
        r -= 1
        this_choice = choices_table[r, c]

best_path.reverse()
print best_path
