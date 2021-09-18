def maxSubsetSum(a):
    dp = [0] * len(a)
    dp[0] = a[0]
    for i in range(1, len(a)):
        dp[i] = max(dp[i-1], dp[i-2]+a[i])
    print(dp)
    return max(dp)


def noofwaystomakechange(n):

    return


print(maxSubsetSum([7, 10, 12, 7, 9, 14]))
