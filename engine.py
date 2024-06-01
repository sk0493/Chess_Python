# This class is responsible for storing all the information about the current game state. 
# Also responsible to determine valid moves. 
# It will keep a move log also

class game_state():
    def __init__(self) -> None:
        # each list represents a row on the chess board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wN", "wR"]
        ]
        self.whiteTurn = True #to be used to check who's turn it is
        self.moveLog = []