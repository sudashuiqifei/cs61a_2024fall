def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)

        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

"""
1,1,2,3,5,8,13,21,34,55
"""
print(fib_tree(1))
print(fib_tree(2))
print(fib_tree(3))

def count_leaves(tree):
    if is_leaf(tree):
            return 1
    else:
        branch_count = [count_leaves(b) for b in branches(tree)]
        return sum(branch_count)

print(count_leaves(fib_tree(5)))
