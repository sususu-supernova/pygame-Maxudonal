import pygame
import sys
from button import Button
import final_game 

pygame.init()

screen = pygame.display.set_mode((1080,750))

#################################################################################

def game_screen() :

    # เปลี่ยนให้ไปเล่นหน้าเกมใน game
    action = final_game.run_game()
    if action == "game" : # เริ่มเกม - ในที่นี้เป็นการคืนค่าของปุ่ม try again
        return "game"
    if action == False : # กลับไปที่หน้าหลัก
        return False

#################################################################################

# หน้าจอเริ่มต้นตอนเข้าเกม
def main_menu() :
    screen.fill("#F3C623")
    pygame.display.set_caption("main menu")

    name_text = pygame.font.SysFont("Inter", 80).render("MAIN MENU", True, "black")
    name_rect = name_text.get_rect(center=(540, 280))
    screen.blit(name_text, name_rect)

    best_text = pygame.font.SysFont("Inter", 24).render("BEST LEVEL", True, "black")
    best_rect = best_text.get_rect(center=(540, 341))
    screen.blit(best_text, best_rect)

    # ปุ่ม START
    start_pic = pygame.image.load("button.png")
    start_button_surface = pygame.transform.scale(start_pic, (300, 140))
    start_button = Button(start_button_surface, 381, 440, "START")

    # ปุ่ม QUIT
    quit_pic = pygame.image.load("button.png")
    quit_button_surface = pygame.transform.scale(quit_pic, (300, 140))
    quit_button = Button(quit_button_surface, 699, 440, "QUIT")

    # ตรวจสอบการคลิก
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # action = start_button.checkForInput(pygame.mouse.get_pos()) # pygame.mouse.get_pos() จะคืนค่าเป็นทูตที่มีสองค่า (x, y) ซึ่งเป็นพิกัดของตำแหน่งปัจจุบันของเมาส์
            if start_button.checkForInput(pygame.mouse.get_pos()) == "game":
                return "game"
            
            quit_button.checkForInput(pygame.mouse.get_pos())

    # อัปเดตและตรวจสอบสีของปุ่ม START และ QUIT
    start_button.changeColor(pygame.mouse.get_pos())  # เปลี่ยนสีข้อความเมื่อเมาส์อยู่เหนือปุ่ม
    quit_button.changeColor(pygame.mouse.get_pos())   # เปลี่ยนสีข้อความเมื่อเมาส์อยู่เหนือปุ่ม

    # แสดงปุ่ม
    start_button.update()
    quit_button.update()

    pygame.display.update()

#################################################################################

# ฟังก์ชันหน้าจอหลัก
def main():

    in_game = False  # กำหนดสถานะเกมเริ่มต้นว่าอยู่ในหน้าหลัก

    while True:
        if not in_game:
            in_game = main_menu()  # ถ้าไม่ได้อยู่ในหน้าเกม ให้แสดงหน้าหลัก
        else:
            in_game = game_screen()  # in_game = "game" ซึ่งเป็น Truthy values

if __name__ == "__main__":
    main()

#################################################################################

    '''screen.fill("Black")
    pygame.display.set_caption("game")

    play_text = pygame.font.SysFont("Inter", 45).render("this is the play screen", True, "white")
    play_rect = play_text.get_rect(center=(540, 250))
    screen.blit(play_text, play_rect)

    # ปุ่ม QUIT สำหรับกลับไปหน้าหลัก
    quit_pic = pygame.image.load("test_button_2.png")
    quit_button_surface = pygame.transform.scale(quit_pic, (369,210)) # กำหนดขนาดกรอบของตัวปุ่น
    quit_button = Button(quit_button_surface,540,400,"QUIT")

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            quit_button.checkForInput(pygame.mouse.get_pos())

    quit_button.changeColor(pygame.mouse.get_pos()) 
    quit_button.update() 

    pygame.display.update()'''