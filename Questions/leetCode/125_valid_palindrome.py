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
def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1

        while i < j and not s[j].isalnum():
            j -= 1

        if not s[i].lower() == s[j].lower():
            return False

        i += 1
        j -= 1

    return True
    
# we could built our own function to determine if the char is alpha numeric
# def alphaNum(self, c):
#    return (ord('a') < ord('c') < ord('z') or 
#            ord('A') < ord('c') < ord('Z') or 
#            ord('0') < ord('c') < ord('9'))

if __name__ == "__main__":
    print(isPalindrome("race a car"))