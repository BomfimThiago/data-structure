"""
given 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all
adjacent same colored pixels with the given color

example:
Input:
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 2, 2, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 2, 2, 0},
               {1, 1, 1, 1, 1, 2, 1, 1},
               {1, 1, 1, 1, 1, 2, 2, 1},
               };
    x = 4, y = 4, newColor = 3
The values in the given 2D screen
  indicate colors of the pixels.
x and y are coordinates of the brush,
   newColor is the color that
should replace the previous color on 
   screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 3, 3, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 3, 3, 0},
               {1, 1, 1, 1, 1, 3, 1, 1},
               {1, 1, 1, 1, 1, 3, 3, 1},
               };
"""
def helper(screen, x, y, prevC, newC):
    # base case
    ROWS, COLS = len(screen), len(screen[0])
    if ( x < 0 or x > ROWS - 1 or y < 0 or y > COLS - 1 or screen[x][y] != prevC or screen[x][y] == newC):
        return
    # basically the x, y can not be all of bounds
    # I can not try to change other color then they the prevC
    # I dont neet to change the color if it's already newC

    # replace color:
    screen[x][y] = newC

    # recur to all the adjacents (top, bottom, left, right)
    helper(screen, x + 1, y, prevC, newC)
    helper(screen, x - 1, y, prevC, newC)
    helper(screen, x, y + 1, prevC, newC)
    helper(screen, x, y - 1, prevC, newC)

    return screen


def floodFill(screen, x, y, newC):
    prevC = screen[x][y]

    if(prevC == newC):
        return # probably not gonna happen but just in case
    return helper(screen, x, y, prevC, newC)


if __name__ == "__main__":
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
        ]
    x = 4
    y = 4
    newColor = 3
    print(screen)
    print(floodFill(screen, x, y, newColor))