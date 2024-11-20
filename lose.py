# lose.py
import pygame
from button import Button

pygame.init()

screen = pygame.display.set_mode((1080,750))
bg_image = pygame.image.load("lose_bg.png")

def lose(screen):

    '''main menu + try again'''

    while True:

        screen.blit(bg_image, (0, 0))
     
        ###########################################################################

        try_pic = pygame.image.load("button.png")
        try_button_surface = pygame.transform.scale(try_pic, (340, 200))
        try_button = Button(try_button_surface, 351, 630, "TRY AGAIN")

        ###########################################################################

        main_manu_pic = pygame.image.load("button.png")
        main_manu_button_surface = pygame.transform.scale(main_manu_pic, (340, 200))
        main_manu_button = Button(main_manu_button_surface, 729, 630, "MAIN MENU")

        ###########################################################################
 
        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN : 

                if main_manu_button.checkForInput(pygame.mouse.get_pos()) ==  False :
                    return False  # ส่งค่ากลับไปที่หน้าหลัก
                
                # action = try_button.checkForInput(pygame.mouse.get_pos())
                if try_button.checkForInput(pygame.mouse.get_pos()) == "game" :
                    return "game"
                
        ###########################################################################
 
        try_button.changeColor(pygame.mouse.get_pos())
        main_manu_button.changeColor(pygame.mouse.get_pos())

        try_button.update()
        main_manu_button.update()

        pygame.display.update()  # อัพเดตหน้าจอ