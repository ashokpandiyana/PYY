def isPalindrome(S):
    palindrome = ''
    for i in S:
        palindrome = i + palindrome
    return 1 if S == palindrome else 0


def duplicates(s):
    dicti = {}
    result_values = []
    for i in s:
        if i in dicti.keys():
            dicti[i] += 1
        else:
            dicti[i] = 1
    for j in dicti.keys():
        if dicti[j] >= 2:
            result_values.append(j)
    return result_values


def rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s2)):
            s3 = s2[i:] + s2[:i]
            if s3 == s1:
                return True
    return False


def anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def reverse(s):
    res = ''
    for i in s:
        res = i + res
    return res


print(isPalindrome("gog"))
print(duplicates("test string"))
print(rotation("GEEKS", "EKSGE"))
print(rotation("ABACD", "CDABA"))
print(anagram("listen", "silent"))
print(reverse("ABCD"))
