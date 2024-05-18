"""
20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
def isValid(s: str) -> bool:
    closeToOpen = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
   
    stack = []
    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False
    
def isValid2(s: str) -> bool:
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []

    for brack in s:
        # if its a open bracket
        if brack in brackets:
            stack.append(brack)
            continue

        if not stack:
            return False

        # if its a close bracket
        openB = stack.pop()
        if not brack == brackets[openB]:
            return False
    
    if stack:
        return False

    return True



if __name__ == "__main__":
    print(isValid2("(])"))

