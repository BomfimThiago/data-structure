"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:
-2**31 <= x <= 2**31 - 1
"""
import math


def reverse(x: int) -> int:
    # if its a signed 32-bit then the number should be in this range -2147483648 <= num <= 2147483647
    # ou para usar o valor que ele deu -2**31 <= x <= 2**31 - 1
    MIN = -2147483648
    MAX = 2147483647

    y = 0
    while x: # while this integer is not 0
        digit = int(math.fmod(x, 10)) # % doesnt work well with negative integers
        x = int(x / 10) # again, convert to int because python is dumb

        if (y > MAX // 10 or (y == MAX // 10  and digit >= MAX % 10)):
            return 0
        
        if (y < MIN // 10 or (y == MIN // 10 and digit <= MIN % 10)):
            return 0

        y = (y * 10) + digit

    return y

if __name__ == "__main__":
    print(reverse(-1563847412))