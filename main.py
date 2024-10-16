import pygame
from game import gameLoop

# Initialize pygame before any other pygame module is used
pygame.init()

if __name__ == "__main__":
    gameLoop()

# Quitting pygame when the program ends
pygame.quit()
