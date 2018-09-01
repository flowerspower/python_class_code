"""
ID: s.sophi1
LANG: PYTHON2
PROG: barn1
"""

input = open('barn1.in', 'r')
output = open('barn1.out', 'w')
strings = input.readlines()
strings = [string.rstrip() for string in strings]
boards, stalls, full_stall_count = [int(x) for x in strings[0].split()]
full_stalls = [int(s) for s in strings[1:]]
full_stalls = sorted(full_stalls)
input.close()


def find_boarders(used_stalls):
    gaps = []
    for i in range(full_stall_count-1):
        gaps.append(used_stalls[i+1]-used_stalls[i])
    gaps = sorted(gaps)
    if boards != 1:
        largest_gaps = gaps[-boards+1:]
    else:
        largest_gaps = []
    stall_count = (used_stalls[-1] - used_stalls[0]) + 1
    if boards > full_stall_count:
        return full_stall_count
    else:
        return (stall_count - sum(largest_gaps)) + boards - 1


output.write(str(find_boarders(full_stalls)) + '\n')
output.close()
