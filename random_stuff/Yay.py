"""
ID: s.sophi1
LANG: PYTHON2
TASK: test
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
string = fin.readline()
a = string.split()
sum = int(a[0]) + int(a[1])
fout.write (str(sum) + '\n')
fout.close()
