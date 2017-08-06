import random
import time



numbers = []
for i in range(1000000):
    numbers.append(random.randint(1, 10000000))

numbers = sorted(numbers)

def linearsearch(num_list, x):
    index = 0
    for num in num_list:
        if num == x:
            return index
        index += 1
    return None

start_time = time.time()
print linearsearch(numbers, 2)
print("%s seconds" % (time.time() - start_time))


def binary_search(a_list, item):
    first = 0
    last = len(a_list)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        mid_number = a_list[midpoint]
        if a_list[midpoint] == item:
            found = True
            return midpoint
        else:
            if item < mid_number:
                last = midpoint-1
            else:
                first = midpoint+1
    return None

start_time = time.time()
print binary_search(numbers, 10)
print("%s seconds" % (time.time() - start_time))