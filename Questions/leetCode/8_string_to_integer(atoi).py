"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed 
integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or 
positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. 
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

"""
def myAtoi(s: str) -> int: 
    # rules
    # 1 ignore leading spaces = s.trim()
    # check for "-" or "+" to see if its negative or positve
    # read the next until a non digit is find, the rest is ignored
    # convert to an integer
    # if no digits then its 0
    # if the integer is out of bound, then clamp the integer so it remains in the range
    # return the integer

    MAX = 2147483647
    MIN = -2147483648

    y = 0
    i = 0

    while i < len(s) and s[i] == " ":
        i += 1

    # verify if s[i] is out of bound, it means that the string only has spaces
    if i > len(s) - 1:
        return 0

    sign = 1
    if s[i] == "-": # the next character after spaces must be a sign(if there is a sign)
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1
    elif not s[i].isdigit(): # next letter after spaces is another letter, so just return 0
        return 0

    for char in s[i:]:
        if not char.isdigit():
            break
        
        digit = int(char)
        if sign == 1 and y > (MAX - digit) / 10:
            return MAX
        elif sign == -1 and sign * y < (MIN + digit) / 10:
            return MIN
        
        y = (y * 10) + digit


    return sign * y

if __name__ == "__main__":
    print(myAtoi("42"))