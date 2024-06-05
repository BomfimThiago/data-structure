"""
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.
"""
def minCut(A):
    # aba
    # aab

    l = 0
    r = len(A) - 1
    count = 0
    while l < r and A[l] == A[r]:
        l += 1,
        r += 1
    else:
        count += minCut(A[l+1:r])
        count += minCut(A[l:r - 1])

    return count

if __name__ == "__main__":
    A = "aab"
    print(minCut(A))