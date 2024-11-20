# win.py
import pygame
from button import Button

pygame.init()

screen = pygame.display.set_mode((1080,750))
bg_image = pygame.image.load("win_bg.png")

def win(screen):

    '''main menu + next level'''

    while True : 

        screen.blit(bg_image, (0, 0))
        
        ###########################################################################

        next_pic = pygame.image.load("button.png")
        next_button_surface = pygame.transform.scale(next_pic, (340, 200))
        next_button = Button(next_button_surface, 351, 630, "NEXT LEVEL")

        ###########################################################################

        main_manu_pic = pygame.image.load("button.png")
        main_manu_button_surface = pygame.transform.scale(main_manu_pic, (340, 200))
        main_manu_button = Button(main_manu_button_surface, 729, 630, "MAIN MENU")

        ###########################################################################

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # action = main_manu_button.checkForInput(pygame.mouse.get_pos())
                if main_manu_button.checkForInput(pygame.mouse.get_pos()) ==  False :
                    return False  # ส่งค่ากลับไปที่หน้าหลัก
                
                # action = next_button.checkForInput(pygame.mouse.get_pos())
                if next_button.checkForInput(pygame.mouse.get_pos()) ==  "game" :
                    return "game"
                
        ###########################################################################

        next_button.changeColor(pygame.mouse.get_pos())
        main_manu_button.changeColor(pygame.mouse.get_pos())

        next_button.update()
        main_manu_button.update()

        pygame.display.update()  # อัพเดตหน้าจอ
