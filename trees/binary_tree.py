# represent a parse tree with a 3-tuple : (oprand, leftsubtree, rightsubtree)
# leaf nodes are represented with a number

binary_parse_tree1 = ('+', 3, ('*', 4, 5))
binary_parse_tree2 = ("+", ("/", 3, 2), ("*", 5, 6))

def tree_height(t):
    if isinstance(t, tuple):
        left_substre_height = tree_height(t[1])
        right_substre_height = tree_height(t[2])
        return 1 + max(left_substre_height, right_substre_height)
    else:
        return 0

print tree_height(binary_parse_tree1)
print tree_height('+')

def tree_leaves(t):
    if isinstance(t, tuple):
        left_subtree_leaves = tree_leaves(t[1])
        right_subtree_leaves = tree_leaves(t[2])
        return left_subtree_leaves + right_subtree_leaves
    else:
        return 1
print tree_leaves(binary_parse_tree2)
print tree_leaves(binary_parse_tree1)