"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""
# aaba"
def contSubstrings(s):
    count = 0 
    for i in range(len(s)):
        # odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1

        # even
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1

    return count



if __name__ == "__main__":
    print(contSubstrings("aaa"))