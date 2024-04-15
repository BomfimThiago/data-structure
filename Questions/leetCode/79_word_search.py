"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    path = set()
    ROWS, COLS = len(board), len(board[0])

    def dfs(i, r, c):
        if i == len(word):
            return True
        if ((r < 0 or c < 0) or (r > ROWS or c > COLS) or (r, c) in path or board[r][c] != word[i]):
            return False
        

if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], 
    word = "ABCCED"
    print(exist(board, word))