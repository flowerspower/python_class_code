from collections import deque

matching_stuff = {'(' : ')','[' : ']','{' : '}'}


def is_matched(parentheses_str):
    stack = []
    for p in parentheses_str:
        if p in matching_stuff.keys():
            stack.append(p)
        elif p in matching_stuff.values():
            if stack and matching_stuff[stack[-1]] == p:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def bfs_search_min_deletions(initial_string):
    frontier = deque([initial_string])
    explored = set([])

    while (frontier):
        current_node = frontier.popleft()
        current_state = current_node
        #    print current_state

        if is_matched(current_state):
            print('solution found:')
            print(current_state)
            return len(initial_string) - len(current_state)

        explored.add(tuple(current_state))
        for i in range(len(current_state)):
            child_state = current_state[:i] + current_state[i+1:]

            if str(child_state) not in explored:
                frontier.append(child_state)

    print('solution not found')
    return


print(bfs_search_min_deletions('()[](){((()))}'))
print(bfs_search_min_deletions('[[()](({()}))]'))
print(bfs_search_min_deletions('(]'))
print(bfs_search_min_deletions(')[]('))
print(bfs_search_min_deletions(''))
print(bfs_search_min_deletions('()))))'))
print(bfs_search_min_deletions('unicorn'))
