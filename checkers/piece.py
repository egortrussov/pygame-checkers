import pygame
from .constants import BLACK, RED, BLUE, WHITE, GREY, SQUARE_SIZE, YELLOW

class Piece:
    PADDING = 10
    BORDER = 2
    CROWN_RADIUS = 10
    HINT_RADIUS = 15

    def __init__(self, row, col, color, is_hint=False):
        self.row = row 
        self.col = col 
        self.color = color 
        self.king = False
        self.is_hint = is_hint

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1
        
        self.x = 0 
        self.y = 0 
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2;
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2;
    
    def make_king(self):
        self.king = True 
    
    def draw(self, win):
        self.calc_pos()
        if self.is_hint:
            pygame.draw.circle(win, BLUE, (self.x, self.y), self.HINT_RADIUS)
            return;

        radius = SQUARE_SIZE // 2  - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(win, YELLOW, (self.x, self.y), self.CROWN_RADIUS)
    
    def __repr__(self):
        return str(self.color)
    
    def move(self, row, col):
        self.row = row 
        self.col = col 
        print('lo')
        self.calc_pos() 