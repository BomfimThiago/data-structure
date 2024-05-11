"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    hashS1 = {}
    for char in s1:
        hashS1[char] = 1 + hashS1.get(char, 0)

    hashWindow = {}
    l = 0
    r = len(s1) - 1
    for i in range(l, r + 1):
        hashWindow[s2[i]] = 1 + hashWindow.get(s2[i], 0)

    while r < len(s2):
        if hashWindow == hashS1:
            return True
        
        hashWindow[s2[l]] -= 1
        if hashWindow[s2[l]] == 0:
            del hashWindow[s2[l]]

        l += 1
        r += 1

        if r < len(s2):
            hashWindow[s2[r]] = 1 + hashWindow.get(s2[r], 0)

    return False


if __name__ == "__main__":
    print(checkInclusion(s1 = "adc", s2 = "dcda"))