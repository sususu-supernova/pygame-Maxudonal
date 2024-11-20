import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1080,750))
main_font = pygame.font.SysFont("Inter",55)

dark_brown = (89,33,1)
green = (70,112,0)
red = (220,9,0)

class Button() :

    def __init__(self, image, x_pos, y_pos, text_input) :
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True , dark_brown)
        self.text_rect = self.text. get_rect(center=(self.x_pos, self.y_pos))

    def update(self) :
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position) :
        if self.rect.collidepoint(position) :

            if self.text_input == "QUIT":
                pygame.quit()
                sys.exit()

            if self.text_input == "START" :
                return "game"
            
            if self.text_input == "TRY AGAIN" :
               return "game"
            
            if self.text_input == "MAIN MENU" :
                return False
            
            if self.text_input == "NEXT LEVEL" :
                return "game"
            
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) :
            if self.text_input == "START" or self.text_input ==  "TRY AGAIN" or  self.text_input == "NEXT LEVEL" :
                self.text = main_font.render(self.text_input, True , green)
            else :
                self.text = main_font.render(self.text_input, True , red)