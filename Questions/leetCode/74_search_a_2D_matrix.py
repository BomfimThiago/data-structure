"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS = len(matrix)

    # 3 rows
    matrix_l = 0
    matrix_r = ROWS - 1

    while matrix_l <= matrix_r:
        row = (matrix_r + matrix_r) // 2

        # binary search in the row
        l = 0
        r = len(matrix[row]) - 1
    
        while l <= r:
            col = (r + l ) // 2
            if target > matrix[row][col]:
                l = col + 1
            elif target < matrix[row][col]:
                r = col - 1
            else:
                return True
            
        # the previous row
        if target < matrix[row][0]:
            matrix_r = row - 1
        # the next row
        elif target > matrix[row][-1]:
            matrix_l = row + 1
        else:
            return False
        

    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    matrix_2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target_2 = 13
    print(searchMatrix(matrix_2, target_2))