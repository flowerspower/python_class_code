"""
ID: s.sophi1
LANG: PYTHON3
PROG: holstein
"""
import itertools

input = open('holstein.in', 'r')
output = open('holstein.out', 'w')
lines = input.readlines()
input.close()

input_list = [string.strip() for string in lines]
vitamin_count = int(input_list[0])
vitamin_requirements = [int(x) for x in lines[1].split()]
feed_count = int(lines[2])
feed_nutrition = []

for z in range(feed_count):
    feed_nutrition.append([int(z) for z in lines[z+3].rstrip().split()])


def find_best_combination():
    for i in range(feed_count):
        for combination in list(itertools.combinations(range(feed_count), i+1)):
            if check_combination(combination):
                return combination


def check_combination(combination):
    for i in range(vitamin_count):
        this_vitamin_sum = 0
        for feed_index in combination:
            nutritions = feed_nutrition[feed_index]
            this_vitamin_sum += nutritions[i]
        if this_vitamin_sum < vitamin_requirements[i]:
            return False
    return True


answer = find_best_combination()
output.write(str(len(answer)) + " " + ' '.join([str(x+1) for x in answer])+"\n")
output.close()
