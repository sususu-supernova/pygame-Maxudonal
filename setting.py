import pygame

pygame.init()

screen_w = 1080
screen_h = 750
#varible for screen window

white = (255,255,255)
black = (10,10,10)
green = (0,255,0,250)
red = (255,0,0,250)
blue = (0,0,255)
yellow = (255,255,0)
brown = (106,78,66)
sky = (135,206,235)
grass = (132,192,17)
dirt = (155,118,83)
#color variable

font = pygame.font.Font(None, 36)
#set font

screen = pygame.display.set_mode((screen_w,screen_h))
#create screen window


clock = pygame.time.Clock()
#creat time for movement speed refernce
tick = 130

# BG
game_bg_image = pygame.image.load("game_bg.png")