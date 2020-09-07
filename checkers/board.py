import pygame 
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None 
        self.red_left = self.white_left =12 
        self.red_kings = self.white_kings = 0 

    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        board = []
        for row in range(ROWS):
            board.append([])
            if row >= 3 and row < ROWS - 3:
                board[row] = [0] * COLS
                continue 
            for col in range(COLS):
                if row % 2 != col % 2:
                    color = WHITE
                    if row > 3:
                        color = BLACK
                    new_piece = Piece(row, col, color)
                    new_piece.calc_pos()
                    board[row].append(new_piece)
                else:
                    board[row].append(None)
        self.board = board
    
    def draw_pieces(self, win):
        # print(len(self.board[0]))
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 != col % 2 and self.board[row][col]:
                    self.board[row][col].draw(win)
