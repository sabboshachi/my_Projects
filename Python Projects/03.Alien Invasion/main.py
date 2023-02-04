import sys
import pygame

def run_game():
    # Initialize game and creat a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion!")