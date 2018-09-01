"""
ID: s.sophi1
LANG: PYTHON3
PROG: ariprog
"""

input = open('ariprog.in', 'r')
output = open('ariprog.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
search_length = int(strings[0])
pq_limit = int(strings[1])
input.close()

bisquare_set = set()
for p in range(pq_limit+1):
    for q in range(p, pq_limit+1):
        bisquare_set.add(p*p+q*q)
print(bisquare_set)


def try_all_possibilities(bisquares):
    a_and_bs = set()
    bisquares_list = sorted(bisquares)
    for i in range(0, len(bisquares)-search_length+1):
        a = bisquares_list[i]
        num = bisquares_list[-1]-bisquares_list[0]
        for j in range(1, int((num-a)/(search_length-1)+1)):
            b = j
            bad = False
            for x in range(search_length-1, 0, -1):
                if a + (x*b) not in bisquares:
                    bad = True
                    break
            if not bad:
                a_and_bs.add((a, b))
    return a_and_bs


thing = sorted(try_all_possibilities(bisquare_set), key = lambda x: (x[1], x[0]))
if thing:
    for item in thing:
        output.write(str(item[0]) + ' ' + str(item[1]) + '\n')
else:
    output.write('NONE' + '\n')
output.close()
