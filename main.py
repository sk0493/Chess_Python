# Here is is main driver file. This is where code for user input and displaying current Game state object.
import pygame as pg
import engine

# Initialise Pygame
pg.init()

width = height = 400
dimension = 8 # dimension of a chess board is 8x8
sq_size = height / dimension
images = {} # global dictionary of images

def load_images():
    # Using pygame to load in the chess images
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bN", "bR", "bP", "wR", "wN", "wB", "wQ", "wK", "wN", "wR"]
    for piece in pieces:
        images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (sq_size,sq_size))


def draw_game_state(screen, gs):
    '''
    Responsible for all the graphics whtin a current game state. 
    Draws the checkers on the board and pieces.
    '''
    draw_board(screen)
    draw_pieces(screen, gs.board) # draw chess pieces on top of board


def draw_board(screen):
    colours = [pg.Color("white"), pg.Color("brown")]
    for row in range(dimension):
        for column in range(dimension):
            colour = colours[((row+column) % 2)]
            pg.draw.rect(screen, colour, pg.Rect(column*sq_size, row*sq_size, sq_size, sq_size))


def draw_pieces(screen, board):
    pass

def main():
    '''
    Main driver for the code. This will handle user input and update the graphics
    '''

    screen = pg.display.set_mode((width,height))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = engine.game_state()
    load_images()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        
        draw_game_state(screen, gs)
        clock.tick(15)
        pg.display.flip()



if __name__ == "__main__":
    main()

    

