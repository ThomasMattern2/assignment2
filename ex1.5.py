import timeit
import matplotlib.pyplot as plt

def func(n, memoization={}):
    if n in memoization:
        return memoization[n]
    if n == 0 or n == 1:
        memoization[n] = n
        return n
    memoization[n] = func(n-1, memoization) + func(n-2, memoization)
    return memoization[n]
def func2(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
xaxis = [n for n in range(36)]
newfunctimes = [timeit.timeit(lambda: func(n), number= 1) for n in range(36)]
oldfunctimes = [timeit.timeit(lambda: func2(n), number= 1) for n in range(36)]
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(xaxis, newfunctimes, 'g', label='Optimized time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Optimized Time vs. Range of Values')
ax1.set_title('Range of values (0-35)')
ax1.legend()

ax2.plot(xaxis, oldfunctimes, 'r', label='Original time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Original Time vs. Range of Values')
ax2.set_title('Range of values (0-35)')
ax2.legend()

plt.show()