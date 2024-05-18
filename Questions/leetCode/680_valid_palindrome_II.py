"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

"""

def validPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            # novos array skipando l or r
            skipL = s[l + 1: r + 1] # move l + 1 
            skipR = s[l:r] # move l - 1
            # compara as duas strings ao contrário
            return skipL == skipL[::-1] or skipR == skipR[::-1]
        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    print(validPalindrome("cbbcc"))