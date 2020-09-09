import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE, YELLOW

class Piece:
    PADDING = 10
    BORDER = 2
    CROWN_RADIUS = 10

    def __init__(self, row, col, color):
        self.row = row 
        self.col = col 
        self.color = color 
        self.king = False

        if self.color == RED:
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
        self.calc_pos() 