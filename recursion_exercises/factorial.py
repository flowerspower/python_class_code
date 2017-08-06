# recursive function that calculates factorials
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(999)


def factorial2(n):
    def tail_helper(n, acc):
        if n == 1:
            return acc
        else:
            return tail_helper(n-1, acc * n)

    return tail_helper(n, 1)

print factorial2(998)
