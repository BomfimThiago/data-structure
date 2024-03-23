"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = ["" for _ in range(numRows)]
    i = 0
    direction = -1

    for char in s:
        res[i] += char
        if i == 0 or i == numRows - 1:
            direction *= -1
        i += direction

    return "".join(res)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))

# This function `convert(s: str, numRows: int) -> str` is used to convert a string `s` into a zigzag pattern on a given number of rows and then read line by line.

# Here's a step-by-step explanation:

# 1. If `numRows` is 1, the function returns the original string `s` because the zigzag pattern on one row is the string itself.

# 2. `res = ["" for _ in range(numRows)]`: This line initializes `res`, a list of empty strings. Each string in `res` represents a row in the zigzag pattern.

# 3. `i = 0` and `direction = -1`: These lines initialize the row index `i` and the direction of movement. The direction is initially set to -1.

# 4. The `for` loop iterates over each character in the string `s`. For each character:

#    - `res[i] += char`: The character is added to the current row `i`.

#    - `if i == 0 or i == numRows - 1: direction *= -1`: If the current row `i` is the first or the last row, the direction of movement is reversed. This is how the zigzag pattern is achieved.

#    - `i += direction`: The row index `i` is updated according to the direction of movement.

# 5. Finally, `return "".join(res)`: The rows of the zigzag pattern are joined together into a single string and returned. The rows are read from top to bottom.s