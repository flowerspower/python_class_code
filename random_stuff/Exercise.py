import random
import numpy as np
# list = []
# count = {}
#
# for i in range(100):
#     x = random.randint(1, 10)
#     list.append(x)
#     if x in count:
#         count[x] += 1
#     else:
#         count[x2] = 1
#
# print list
# print count
Lose = 0
Win = 0
play_round_limit = 10000
play_round = 1

def spin_once():
    result = np.random.choice(['Lose', 'Win', 'Again'], p=[0.5, 0.125, 0.375])
    return result

while (play_round <= play_round_limit):
    r = spin_once()
    if r == 'Lose':
        Lose += 1
        play_round += 1
    elif r == 'Win':
        Win += 1
        play_round += 1

print 'Win times: ', Win
print 'Lose times: ', Lose