
def func(n, memoization={}):
    if n in memoization:
        return memoization[n]
    if n == 0 or n == 1:
        memoization[n] = n
        return n
    memoization[n] = func(n-1, memoization) + func(n-2, memoization)
    return memoization[n]
