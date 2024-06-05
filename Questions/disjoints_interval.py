"""
Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.
"""
def solve(A):
    sorted_A = sorted(A, key=lambda item: item[1]) # order by the ends, and then compare the ends
    disjoint_list_max_size = 1
    end = sorted_A[0][1] # end of the first point
    for i in range(1, len(sorted_A)):
       if sorted_A[i][0] > end: # the beggining of the next point must be higher then the end of the previous one
           disjoint_list_max_size += 1
           end =  sorted_A[i][1]
    return disjoint_list_max_size

        
if __name__ == "__main__":
    A=[
    [4, 4],
    [8, 15],
    [6, 6],
    [2, 13],
    [2, 12]
    ]
print(solve(A))