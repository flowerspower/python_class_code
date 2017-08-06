def print_all_paths(rows, cols, allpaths):
    if rows == 0 and cols == 0:
        print allpaths
        return
    if rows == 0 and cols > 0:
        for i in range(cols):
            allpaths += 'e '
        print allpaths
        return
    if rows > 0 and cols == 0:
        for i in range(rows):
            allpaths += 's '
        print allpaths
        return
    print_all_paths(rows, cols-1, allpaths + 'e ')
    print_all_paths(rows-1, cols, allpaths + 's ')


# print_all_paths(10, 10, '')

# returns a list of strings representing all possible paths through a r x c grid from
# upper left corner to lower right corner when only eastward and southward moves are allowed
def find_all_paths(r, c):
    if r == 0 and c == 0:
        return []
    if r == 0 and c > 0:
        path = ''
        for i in range(c):
            path += 'E '
        return [path]
    if r > 0 and c == 0:
        path = ''
        for i in range(r):
            path += 'S '
        return [path]
    sub_solution_1 = find_all_paths(r, c-1)
    sub_solution_2 = find_all_paths(r-1, c)
    mysolution = []
    for s in sub_solution_1:
        mysolution.append('E ' + s)
    for x in sub_solution_2:
        mysolution.append('S ' + x)
    return mysolution

all_paths = find_all_paths(10, 10)
print 'there are ' + str(len(all_paths)) + ' possible paths'
for p in find_all_paths(10, 10):
   print p
