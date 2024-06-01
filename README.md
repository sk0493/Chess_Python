# Introduction

- Ongoing project. Building a chess game on Python.

## Requirements

- Pygame

# TODO

- [x] Drawing the board and pieces 
- [ ] Moving the pieces 

# Code Documentation

## Setting up the game state

```Python
class game_state():
    def __init__(self) -> None:
        # each list represents a row on the chess board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteTurn = True #to be used to check who's turn it is
        self.moveLog = []
```

- 2d 8x8 board
- Could have used numpy array instead
- First character represents colour of piece (white or black)
- Second character represents type of the piece (Standard Chess notation)
- "--" represents an empty space
- Decided for these names as these are what the respective images are called 
- Using a list of lists means it will be easier for me to access items later (such as when drawing the pieces)

## Drawing the chess board and pieces

```Python
def draw_game_state(screen, gs):
    '''
    Responsible for all the graphics whtin a current game state. 
    Draws the checkers on the board and the pieces.
    '''
    draw_board(screen, gs.board)

def draw_board(screen, board):
    colours = [pg.Color("white"), pg.Color("brown")]
    for row in range(dimension):
        for column in range(dimension):
            colour = colours[((row+column) % 2)]
            pg.draw.rect(screen, colour, pg.Rect(column*sq_size, row*sq_size, sq_size, sq_size))
            piece = board[row][column]
            if piece != "--": # not empty cell
                screen.blit(images[piece], pg.Rect(column*sq_size, row*sq_size, sq_size,sq_size))

```

It's important to draw the chess board before the chess pieces, order matters.
Pygame has built in functions that we can use to "draw" a screen (Rect method) and load in images.

In a standard chess board, the color of the cells alternates between white and black in a checkerboard pattern. Whether a cell is white or black depends on both its row and column indices. The top left cell is always white. 

It is a 8x8 grid and the cells can be indexed starting from (0,0) to (7,7). Using a for loop and checking the parity (even or odd) is used to draw the checkboard pattern. 
- If the sum of the row index and column index is even, the cell is white.
- If the sum of the row index and column index is odd, the cell is black.

For example: 

- Cell (0,0): 0 + 0 = 0 (even) - White
- Cell (0,1): 0 + 1 = 1 (odd) - Black
- Cell (1,1): 1 + 1 = (even) - White

Since the result of `(row+column) % 2)` will either be 0 or 1, variable "colour" is used to index the list "colours", which is used to draw the cell either white or black.

It is iterating and drawing each cell until the end of the board's dimension is reached. 

Similarly for the actual chess pieces, we are indexing the items in the "board" variable in engine.py

- Looking at the cell (for example (1,2), which is position of "bP"), if the cell is not empty ("--") then by using `screen.blit` method, the respective chess piece is drawn over the chess board.
- This is why using a list of lists, iteration and naming each chess pieces as they are named in the images folder was required as it made this step easier.