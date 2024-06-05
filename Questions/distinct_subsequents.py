"""
Given two sequences A, B, count number of unique ways in sequence A, 
to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer representing the answer as described in the problem statement.
"""
# brute force
def numDistinct(A, B):
    if A == B:
        return 1 
    if A and not B:
        return 0
    if not A and not B:
        return 1

    count = 0
    for i in range(len(A)):
        string = A[:i] + A[i + 1:]
        if string == B:
            count += 1

    return count

# dynamic programming
def numDistinct(A, B):
    cache = {}
    def dfs(i, j):
        if j == len(B):
            return 1
        if i == len(A):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        
        if A[i] == B[j]:
            cache[(i, j)] = dfs(i +1, j + 1) + dfs(i + 1, j)
        else:
            cache[(i, j)] = dfs(i + 1, j)
        return cache[(i, j)]
    return dfs(0, 0)

if __name__ == "__main__":
    A = "rabbbit" 
    B = "rabbit"
    print(numDistinct(A, B))