# win.py
import pygame
from button import Button

pygame.init()

# กำหนดขนาดหน้าจอ
screen_w, screen_h = 1080, 750
white = (255, 255, 255)

def win(screen):

    '''main menu + next level'''

    while True : 

        screen.fill("white")  # เติมหน้าจอเป็นสีดำ

        win_text = pygame.font.SysFont("Inter", 80).render("WIN", True, "black")
        win_rect = win_text.get_rect(center=(540, 297))
        screen.blit(win_text, win_rect)

        ###########################################################################

        next_pic = pygame.image.load("button.png")
        next_button_surface = pygame.transform.scale(next_pic, (360, 140))
        next_button = Button(next_button_surface, 351, 422, "NEXT LEVEL")

        ###########################################################################

        main_manu_pic = pygame.image.load("button.png")
        main_manu_button_surface = pygame.transform.scale(main_manu_pic, (360, 140))
        main_manu_button = Button(main_manu_button_surface, 729, 422, "MAIN MENU")

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
