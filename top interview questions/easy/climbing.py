def climbStairs(n):
    ways = [0]*(n+1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[-1]


print(climbStairs(9))