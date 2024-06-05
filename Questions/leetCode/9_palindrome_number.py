"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
"""
import math
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    div = 1
    
    while x >= 10 * div:
        div *= 10

    # in each iteration mais digit is divide by 100(because Im getting rid of the first and last digit)        
    while x:
        r = x % 10 # 2
        l = x // div # 2

        if l != r:
            return False
        
        x = (x % div) // 10 # chop off the left and right digit
        
        div = div / 100

    return True 
if __name__ == '__main__': 
    print(isPalindrome(121))