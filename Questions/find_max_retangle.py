"""
Max Rectangle in Binary Matrix

Given a 2D binary matrix filled with 0’s and 1’s, find the 
largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
"""
def find_max_retangle(matrix):
    if not matrix:
        return 0
    
    n = len(matrix[0])
    heights = [0] * (n + 1)  # Adicionar um 0 extra para simplificar o código
    max_area = 0
    
    for row in matrix:
        for i in range(n):
            if row[i] == 1:
                heights[i] += 1
            else:
                heights[i] = 0

    return heights

if __name__ == "__main__":
    A = [ [1 ,1 ,1],
          [0 ,0 ,1],
          [1 ,1 ,0] 
        ]
    print(find_max_retangle(A)) # output 4