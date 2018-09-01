lis = [1, 34, 9832, 4, 87, 56, 342]
from random import randint

def my_list_len(l):
    if not l:
        return 0
    return 1 + my_list_len(l[1:])


print(my_list_len(lis))


def count_letters(path, letter):
    count = 0
    for p in path:
        if p == letter:
            count += 1
    return count


def find_all_paths_helper(sq_size, curr_path):
    if len(curr_path) == sq_size*2:
        print(curr_path)
    else:
        if count_letters(curr_path, 'D') < sq_size:
            find_all_paths_helper(sq_size, curr_path+['D'])
        if count_letters(curr_path, 'R') < sq_size:
            find_all_paths_helper(sq_size, curr_path+['R'])


def find_all_paths(sq_size):
    find_all_paths_helper(sq_size, [])


find_all_paths(3)


def potential_super_primes(length, curr_num):
    if len(curr_num) == length:
        print(curr_num)
    else:
        first_num = ['2','3','5','7']
        not_first_num = ['1','3','7','9']
        if len(curr_num) == 0:
            for num in first_num:
                potential_super_primes(length, curr_num+num)
        else:
            for num in not_first_num:
                potential_super_primes(length, curr_num+num)


potential_super_primes(4, '')
