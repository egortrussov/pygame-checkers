import pygame 
from checkers.constants import * 
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True 
    clock = pygame.time.Clock()

    board = Board()

    while (run):
        clock.tick(FPS)

        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                run = False 
            if (e.type == pygame.MOUSEBUTTONDOWN):
                print('down')
                pass
        
        board.draw_cubes(WIN)
        pygame.display.update()

        pass 
    
    pygame.quit()

main()