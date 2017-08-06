mushrooms_and_carrots = [(1,2), (2,1), (3,1), (2,2), (1,0)]
def find_max(mcs):
    current_max = mcs[0]
    for x in mcs:
        value = x[0] + x[1]*2
        current_value = current_max[0] + current_max[1]*2
        if value > current_value:
            current_max = x
    return current_max
print find_max(mushrooms_and_carrots)
def find_max2(mcs):
    if len(mcs) == 1:
        return mcs[0]
    else:
        head = mcs[0]
        tail = mcs[1:]
        tail_max = find_max2(tail)
        head_points = head[0] + head[1]+2
        tail_max_points = tail_max[0] + tail_max[1] +2
        if head_points > tail_max_points:
            return head
        else:
            return tail_max
print find_max2(mushrooms_and_carrots)
max_fib = 10000
all_fibs = []
for i in range(max_fib):
    all_fibs.append(None)
def fib(n):
    if n == 1:
        all_fibs[1]=0
        return 0
    elif n == 2:
        all_fibs[2]=1
        return 1
    else:
        if all_fibs[n-1] != None:
            fib_n_1 = all_fibs[n-1]
        else:
            fib_n_1 = fib(n-1)
            all_fibs[n-1] = fib_n_1
        if all_fibs[n-2] != None:
            fib_n_2 = all_fibs[n-2]
        else:
            fib_n_2 = fib(n-2)
            all_fibs[n-2] = fib_n_2
        return fib_n_1 + fib_n_2
print fib(1000)
