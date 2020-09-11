import pygame 
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None 
        self.red_left = self.white_left =12 
        self.red_kings = self.white_kings = 0 
        self.is_hint_shown = False
        self.current_piece_coords = (None, None)

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
    
    def move(self, start_row, start_col, row, col):
        piece = self.board[row][col]
        print(start_row, start_col, row, col)
        if not piece.is_hint:
            self.remove_hints()
            self.current_piece_coords = (None, None)
            return;
        self.board[start_row][start_col].move(row, col)
        self.board[start_row][start_col], self.board[row][col] =  self.board[row][col], self.board[start_row][start_col]

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1
        
        self.current_piece_coords = (None, None)
        self.remove_hints()
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def remove_hints(self):
        if self.is_hint_shown:
            for row in range(ROWS):
                for col in range(COLS):
                    if self.board[row][col]:
                        if self.board[row][col].is_hint:
                            self.board[row][col] = 0
            self.is_hint_shown = False

    def mark_neighbours(self, piece):
        row, col = piece.row, piece.col

        self.remove_hints()

        self.current_piece_coords = (row, col)
 
        if piece.direction < 0:
            if col > 0 and row > 0 and not self.board[row - 1][col - 1]:
                hint_piece = Piece(row - 1, col - 1, BLUE, True)
                self.is_hint_shown = True
                self.board[row - 1][col - 1] = hint_piece
            if col < COLS - 1 and not self.board[row - 1][col + 1]:
                hint_piece = Piece(row - 1, col + 1, BLUE, True)
                self.is_hint_shown = True
                self.board[row - 1][col + 1] = hint_piece
        else:
            if row < ROWS - 1 and col > 0 and not self.board[row + 1][col - 1]:
                hint_piece = Piece(row + 1, col - 1, BLUE, True)
                self.is_hint_shown = True
                self.board[row + 1][col - 1] = hint_piece
            if col < COLS - 1 and row < ROWS - 1 and not self.board[row + 1][col + 1]:
                hint_piece = Piece(row + 1, col + 1, BLUE, True)
                self.is_hint_shown = True
                self.board[row + 1][col + 1] = hint_piece
        