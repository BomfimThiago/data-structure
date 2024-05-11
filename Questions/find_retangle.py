"""
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel
is a 1 or a 0. The image you get is known to have a single rectangle of 0s on a background of
1s.
Write a function that takes in the image and returns the top-left coordinate, width, and height
of the rectangle of 0's.
Examples:
image1 = [
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1],
]
findRectangle(image1) =>
row: 2, column: 3, width: 3, height: 2
image2 = [
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 0],
]
findRectangle(image2) =>
row: 3, column: 5, width: 2, height: 2
Complexity Analysis variables:
n: number of rows in the input image
m: number of columns in the input image
"""


def findRectangle(image):
    # Get the dimensions of the image
    ROWS, COLS = len(image), len(image[0])
    
    # Initialize variables
    top_row, left_column,  width, height = 0, 0, 0, 0

    # Find the top-left corner of the rectangle
    for i in range(ROWS):
        for j in range(COLS):
            if image[i][j] == 0:
                top_row, left_column = i, j
                break
        else:
            continue
        break 

    if image[top_row][left_column] != 0:
        return None
    
    while top_row + height < ROWS and image[top_row + height][left_column] == 0:
        height += 1
    
    while left_column + width < COLS and image[top_row][left_column + width] == 0:
        width += 1

    return top_row, left_column, width, height

if __name__ == "__main__":
    print(findRectangle([
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
    ]))


