import random
import numpy as np

states = ['sleep', 'eat', 'pick mushrooms', 'dig holes']
state = np.random.choice(states, p=[0.25, 0.25, 0.25, 0.25])

rabbit_states = [state]

for hour in range(24*2000):
    if state == 'sleep':
        state =  np.random.choice(states, p= [0.4, 0.1, 0.3, 0.2])
    elif state == 'eat':
        state = np.random.choice(states, p= [0.2, 0.1, 0.4, 0.3])
    elif state == 'pick mushrooms':
        state = np.random.choice(states, p= [0.4, 0.4, 0.1, 0.1])
    elif state == 'dig holes':
        state = np.random.choice(states, p= [0.4, 0.4, 0.1, 0.1])
    rabbit_states.append(state)

#print rabbit_states

sleep_sleeps = 0
sleep_eats = 0
sleep_mushrooms = 0
sleep_dig = 0
for i in range(len(rabbit_states)-1):
    if rabbit_states[i] + rabbit_states[i+1] == 'sleepsleep':
        sleep_sleeps += 1
    elif rabbit_states[i] + rabbit_states[i+1] == 'sleepeat':
        sleep_eats +=1
    elif rabbit_states[i] + rabbit_states[i+1] == 'sleeppick mushrooms':
        sleep_mushrooms +=1
    elif rabbit_states[i] + rabbit_states[i+1] == 'sleepdig holes':
        sleep_dig +=1

print 'sleep sleep count:', sleep_sleeps
print 'sleep eat count:', sleep_eats
print 'sleep pick mushroom count:', sleep_mushrooms
print 'sleep dig holes count:', sleep_dig
print 'sleep sleep prob:', float(sleep_sleeps)/(sleep_sleeps + sleep_eats + sleep_mushrooms + sleep_dig)
print 'sleep eat prob:', float(sleep_eats)/(sleep_eats + sleep_sleeps + sleep_mushrooms + sleep_dig)
print 'sleep pick mushrooms prob:', float(sleep_mushrooms)/(sleep_eats + sleep_sleeps + sleep_mushrooms + sleep_dig)
print 'sleep dig holes prob:', float(sleep_dig)/(sleep_eats + sleep_sleeps + sleep_mushrooms + sleep_dig)