import pygame 
from checkers.constants import * 
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row, col = x // SQUARE_SIZE, y // SQUARE_SIZE
    return row, col 

def main():
    run = True 
    clock = pygame.time.Clock()

    board = Board()
    board.create_board()

    while (run):
        clock.tick(FPS)

        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                run = False 
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                col, row = get_row_col_from_mouse(pos)
                print(row, col)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)
        
        board.draw_cubes(WIN)
        board.draw_pieces(WIN)
        pygame.display.update()

        pass 
    
    pygame.quit()

main()