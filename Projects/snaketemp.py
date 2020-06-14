import pygame
import time
import random
 
pygame.init()
 
#Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#PyGame Frame Size
dis_width = 600
dis_height = 400
 
#Header
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
#Creates Game Clock
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

#Sets Font Size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 

#Score Keeper
def Your_score(score):
    print()
 
 
#Drawing of Snake
def our_snake(snake_block, snake_list):
    print()
 
#Message printer 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#Loop to keep running the game
def gameLoop():
    #Game Loop Here
    print()
 

#Runs loop Over and Over
gameLoop()