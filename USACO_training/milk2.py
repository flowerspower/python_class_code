"""
ID: s.sophi1
LANG: PYTHON2
PROG: milk2
"""

input = open('milk2.in', 'r')
output = open('milk2.out', 'w')
lines = input.readlines()
input.close()

milk_times = []
milks = int(lines[0].rstrip())

for i in range(milks):
    x, y = lines[i+1].split()
    milk_times.append((int(x), int(y)))


def merge_intervals(intervals):
    intervals = sorted(intervals)
    milk_inters = [intervals[0]]
    for interval in intervals[1:]:
        if milk_inters[-1][1] >= interval[0]:
            milk_inters[-1] = (milk_inters[-1][0], max(interval[1], milk_inters[-1][1]))
        else:
            milk_inters.append(interval)
    print milk_inters
    return milk_inters


def milking_time(intervals):
    longest_time_milk = 0
    for i in range(len(intervals)):
        if intervals[i][1]-intervals[i][0] > longest_time_milk:
            longest_time_milk = intervals[i][1]-intervals[i][0]
    return longest_time_milk


def no_milking_time(intervals):
    no_milk_time = 0
    for i in range(len(intervals)-1):
        if intervals[i+1][0]-intervals[i][1] > no_milk_time:
            no_milk_time = intervals[i+1][0]-intervals[i][1]
    return no_milk_time


output.write(str(milking_time(merge_intervals(milk_times))) + ' ' + str(no_milking_time(merge_intervals(milk_times))) + '\n')
output.close()
