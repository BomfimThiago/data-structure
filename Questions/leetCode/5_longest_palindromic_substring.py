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
    # babad
    # cbbd
    res = [-1, -1]
    resL = 0

    for i in range(len(s)):
        # if its even
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resL:
                res = [l, r]
                resL = r - l + 1
            l -= 1
            r += 1


        # if its odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resL:
                res = [l, r]
                resL = r - l + 1
            l -= 1
            r += 1
    l, r = res
    return s[l:r + 1]


if __name__ == "__main__":
    print(longestPalindrome("babad"))