"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another 
sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 
"""
import copy
def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        
        l += 1 
        r -= 1

    return True


def longestPalindromSubseq(s):
    res = ""
    def dfs(i, curr, curr_size,  cache):
        nonlocal res
        if i >= len(s):
            return 
        
        # if curr in cache:
        #     return

        print("i", i)
        print("curr", curr)
        print("....................")
        if isPalindrome(curr):
            if curr_size > len(res):
                res = copy.copy(curr)

        curr += s[i]
        dfs(i + 1, curr, curr_size + 1, cache)
        curr = curr[:-1]
        dfs(i + 2, curr, curr_size, cache)

        cache.add(i)

    dfs(0, "", 0, set())


if __name__ == "__main__":
    print(longestPalindromSubseq("bbbab"))