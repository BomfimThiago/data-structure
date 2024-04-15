"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
def minWindow(s: str, t: str) -> str:
    if t == "": return ""
    
    # I need to understand how many letters and what letters are in t
    # this way I map all the char and how many of them I have in t
    dict_t, window = {}, {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1

    have, need = 0, len(dict_t)
    res, resL = [-1, -1], float("inf")
    l = 0 # pointer to the first c in the window
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in dict_t and dict_t[c] == window[c]:
            have += 1

        while have == need:
            # update the res
            if (r - l + 1) < resL:
                res = [l, r]
                resL = (r - l + 1)

            # pop from the left of the window
            window[s[l]] -= 1

            if s[l] in dict_t and window[s[l]] < dict_t[s[l]]:
                have -= 1

            l += 1
    l, r = res
    return s[l:r+1] if resL != float("inf") else ""