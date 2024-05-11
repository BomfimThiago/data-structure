"""
Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

"""
def generateParenthesis(n: int):
    stack = [] # is my curr solution
    res = [] # let's store the solutions in string

    # rules
    # I can only add n elements of '(' and ')''
    # I can only add a close parentheses ')' if I already have a open one '('
    # which mean I can only add ')' if the number of '(' is bigger

    def backtrack(openN, closedN):
        # base case
        if openN == closedN == n:
            res.append("".join(stack))

        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closedN)
            # pop the value from the stack to not interfere with other possibilities
            stack.pop()

        if closedN < openN and closedN < n:
            stack.append(')')
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
    

if __name__ == "__main__":
    print(generateParenthesis(3))