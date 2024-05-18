"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""
def isAlphaNum(char):
    return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z') or ord('1') <= ord(char) <= ord('9')

def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1 
    # s = "A man, a plan, a canal: Panama"
    while l <= r:
        while l < r and not isAlphaNum(s[l]):
            l += 1

        while r > l and not isAlphaNum(s[r]):
            r -= 1

        if l > r:
            return False
        
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
        
    return True
    
# we could built our own function to determine if the char is alpha numeric
# def alphaNum(self, c):
#    return (ord('a') < ord('c') < ord('z') or 
#            ord('A') < ord('c') < ord('Z') or 
#            ord('0') < ord('c') < ord('9'))


if __name__ == "__main__":
    print(isPalindrome(s = "A man, a plan, a canal: Panama"))