"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

"""
def isMatch(s: str, p: str) -> bool:
    # rules
    # 1. '.' matches any single character
    # 2. '*' matches zero or more of the preceding element
    # 3. the matching should cover the entire input string (not partial)
    # 
    # Example 1:
    # Input: s = "aa", p = "a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".
    # 
    # Example 2:
    # Input: s = "aa", p = "a*"
    # Output: true
    # Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    # 
    # Example 3:
    # Input: s = "ab", p = ".*"
    # Output: true
    # Explanation: ".*" means "zero or more (*) of any character (.)".

    # ghruudae
    # ghru*.ae

    # 1. if p is empty, return True if s is empty, False otherwise
    # 2. if p is not empty, check if the first character of s matches the first character of p
    # 3. if the first character of p is not a wildcard, then we have a simple match on our hands
    if not p:
        return True if not s else False