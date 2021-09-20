# Brute Force Approach O(n^2)
import collections


def containerWithMostWater(a):
    res = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            area = (j-i) * min(a[j], a[i])
            res = max(res, area)
    return res


# Optimal Solution O(n)
def containerWithMostWaterBinary(a):
    res, l, r = 0, 0, len(a)-1
    while(l < r):
        area = (r-l) * min(a[r], a[l])
        res = max(res, area)
        if a[l] < a[r]:
            l += 1
        else:
            r -= 1
    return res


def smallNumber(a):
    res = sorted(a)
    dicti = {}
    result = []
    for i in range(len(res)):
        if res[i] not in dicti:
            dicti[res[i]] = i

    for i in a:
        result.append(dicti[i])
    return result


def majorityElement(nums):
    dicti = {}
    for num in nums:
        if num not in dicti:
            dicti[num] = 1
        if dicti[num] > len(nums)//2:
            return num
        else:
            dicti[num] += 1
# nums.sort() return nums[len(nums)//2]

# Kadane Algorithm


def maxSubArray(a):
    res = curr_sum = 0
    for i in range(len(a)):
        curr_sum = max(a[i], curr_sum+a[i])
        res = max(res, curr_sum)
    return res


def reverseOnlyLetters(s):
    l, r = 0, len(s)-1
    s = list(s)
    while l < r:
        while not s[l].isalpha() and l < r:
            l += 1
        while not s[r].isalpha() and l < r:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)


def longestIncreasingSubsequence(nums):
    N = len(nums)
    dp = [1]*N
    for n in range(N):
        for i in range(n):
            if nums[i] < nums[n]:
                dp[n] = max(dp[n], dp[i]+1)
    return max(dp)


def intersectionOfArrays(a, b):
    c = collections.Counter(a)
    output = []
    for n in b:
        if c[n] > 0:
            output.append(n)
            c[n] -= 1
    return output

def mountainArray(a):
    i = 1
    while i < len(a) and a[i] > a[i-1]:
        i+=1
        



print(containerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(containerWithMostWaterBinary([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(smallNumber([8, 1, 2, 2, 3]))
print(majorityElement([3, 2, 3]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(reverseOnlyLetters("ab-cd"))
print(longestIncreasingSubsequence([0, 3, 1, 6, 2, 2, 7]))
print(intersectionOfArrays([1, 2, 2, 1], [2, 2]))
