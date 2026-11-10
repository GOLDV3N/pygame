import pygame
import random
pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT +1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT +2
BLUE = pygame.color('blue') 
LIGHTBLUE = pygame.color('lightblue') 
DARKBLUE = pygame.color('darkblue') 
YELLOW = pygame.color('yellow') 
MAGENTA = pygame.color('magneta') 
ORANGE = pygame.color('orange') 
WHITE = pygame.color('white') 
class sprite(pygame.sprite.sprite):
    def __init__(self,color,height,width):
        super()__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1])]