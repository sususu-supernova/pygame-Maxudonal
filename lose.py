# lose.py
import pygame
from button import Button

pygame.init()

# กำหนดขนาดหน้าจอ
screen_w, screen_h = 1080, 750
white = (255, 255, 255)

def lose(screen):

    '''main menu + try again'''

    while True:

        screen.fill("white")

        lose_text = pygame.font.SysFont("Inter", 80).render("LOSE", True, "black")
        lose_rect = lose_text.get_rect(center=(540, 297))
        screen.blit(lose_text, lose_rect)
     
        ###########################################################################

        try_pic = pygame.image.load("button.png")
        try_button_surface = pygame.transform.scale(try_pic, (360, 140))
        try_button = Button(try_button_surface, 351, 422, "TRY AGAIN")

        ###########################################################################

        main_manu_pic = pygame.image.load("button.png")
        main_manu_button_surface = pygame.transform.scale(main_manu_pic, (360, 140))
        main_manu_button = Button(main_manu_button_surface, 729, 422, "MAIN MENU")

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