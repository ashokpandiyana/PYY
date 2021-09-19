def maxSubsetSum(a):
    dp = [0] * len(a)
    dp[0] = a[0]
    for i in range(1, len(a)):
        dp[i] = max(dp[i-1], dp[i-2]+a[i])
    print(dp)
    return max(dp)


memo = []


def fib(n):

    if n < 0:
        return "Not Possible"
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
        return n
    else:
        result = fib(n-1) + fib(n-1)
        memo[n] = result
    return result


def noofwaystomakechange(n):

    return


print(maxSubsetSum([7, 10, 12, 7, 9, 14]))
print(fib(5))
