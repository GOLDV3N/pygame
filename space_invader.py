import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_= 10
CLLOISION_DISTANCE =27
pygame.init()
clock = pygame.time.Clock()
screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load("backround galaxy.jpg")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("space invader")
pygame.display.set_icon(pygame.image.load("ufo.png"))
