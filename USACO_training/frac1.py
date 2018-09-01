"""
ID: s.sophi1
LANG: PYTHON3
PROG: frac1
"""
from fractions import Fraction

input = open('frac1.in', 'rU')
output = open('frac1.out', 'w')
N = int(input.read().strip())
input.close()

fracs = set()

for d in range(1, N+1):
    for n in range(1, d):
        fracs.add(Fraction(n, d))

sorted_fracs = sorted(fracs)
sorted_fracs = ['0/1'] + [str(f) for f in sorted_fracs] + ['1/1']

print(sorted_fracs)
for f in sorted_fracs:
    output.write(f + '\n')


output.close()
