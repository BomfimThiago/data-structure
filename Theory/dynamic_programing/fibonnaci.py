"""
build a dynamic fibonnaci function
"""

# TOP DOWN APPROACH
# A top down approach is basically cache some results to avoid desnecessary work
# but this is sometimes not known as a true dynamic programming
def fib(n, cache):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]

# the time complexity is O(n)
# the space time is O(1) tough
def trueDP(n):
    if n <= 2:
        return n

    i = 0 # first number of fibonnaci which is 0
    j = 1 # second number of fibonnaci which is 1
    for k in range(1, n):
        tmp = i
        i = j
        j = j + tmp

    return j

    


if __name__ == "__main__":
    print(fib(32, {}))
    print(trueDP(0))

# fibonnaci numbers
# 0 1 1 2 3 5