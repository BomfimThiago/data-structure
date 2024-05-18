"""
3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
def lengthOfLongestSubstring2(s: str):
    window = set()
    l = 0 # left pointer
    res = 0
    for r in range(len(s)):
        # abcb
        while s[r] in window:
            window.remove(s[l])
            l += 1
        else:
            window.add(s[r])
        
        r += 1
        res = max(res, r - l)

    return res

if __name__ == "__main__":
    print(lengthOfLongestSubstring2(s = "pwwkew"))