"""
5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

 
"""
def longestPalindrome(s: str) -> str:
    # palindrome is a word that is equal reading backwards and fowards
    res = ""
    maxSize = 0

    for i in range(len(s)):
        # ODD length palindromes
        l, r = i, i

        while  l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) >= maxSize:
                res = s[l:r + 1]
                maxSize = r - l + 1

            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1

        while  l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) >= maxSize:
                res = s[l:r + 1]
                maxSize = r - l + 1

            l -= 1
            r += 1

    return res














    # res = ""
    # resLength = 0

    # for i in range(len(s)):
    #     # odd length
    #     l, r = i, i
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if (r - l + 1) > resLength:
    #             res = s[l:r+1]
    #             resLength = r - l + 1

    #         l -= 1
    #         r += 1

    #     # even
    #     l, r = i, i + 1
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if (r - l + 1) > resLength:
    #             res = s[l:r+1]
    #             resLength = r - l + 1

    #         l -= 1
    #         r += 1

    # return res