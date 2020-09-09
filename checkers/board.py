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
                    board[row].append(0)
        self.board = board
    
    def draw_pieces(self, win):
        # print(len(self.board[0]))
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 != col % 2 and self.board[row][col]:
                    self.board[row][col].draw(win)
    
    def move(self, piece, row, col):
        piece.move(row, col)
        self.board[piece.row][piece.col], self.board[row][col] =  self.board[row][col], self.board[piece.row][piece.col]

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1
    
    def get_piece(self, row, col):
        return self.board[row][col]