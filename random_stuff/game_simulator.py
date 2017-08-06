import numpy as np

Lose = 0
Win = 0
play_round_limit = 1000
play_round = 1

def spin_once():
    result = np.random.choice(['Lose', 'Win', 'Again'], p=[0.5, 0.125, 0.375])
    return result

while (play_round <= play_round_limit):
    r = spin_once()
    if r == 'Lose':
        print "simulated play No. " + str(play_round) + ",Lose, -$5"
        Lose += 1
        play_round += 1
    elif r == 'Win':
        print "simulated play No. " + str(play_round) + ",Win, +$5"
        Win += 1
        play_round += 1

print 'Win times: ', Win
print 'Lose times: ', Lose