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
background = pygame.image.load("backround galaxy.jpeg")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("space invader")
pygame.display.set_icon(pygame.image.load("ufo.png"))
playerImg= pygame.image.load('rocket_new.png')
playerImg = pygame.transform.scale(playerImg,((64,64)))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
num_of_enemies = 6
enemyImg , enemyX,enemyY,enemyX_change,enemyY_change = [],[],[],[],[]
ENEMY_SIZE = 50
for i in range(num_of_enemies):
    enemyImg.append(pygame.transform.scale(pygame.image.load("enemy.png",ENEMY_SIZE,ENEMY_SIZE)))
    enemyX.append(random.randint(0,SCREEN_WIDTH,SCREEN_HEIGHT))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletImg = pygame.image.load('bullet_new.png')
bulletImg = pygame.transform.scale(bulletImg, (16,32))
bulletX =0
bulletY =PLAYER_START_Y
bullet_state = "ready"
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
game_over = pygame.font.Font("freesansbold.ttf",64)
running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
       