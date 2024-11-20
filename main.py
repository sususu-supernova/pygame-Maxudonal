import pygame
import sys
from button import Button
import final_game 

pygame.init()

###########################################################################

class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 750))
        self.bg_image = pygame.image.load("BG.png")
        self.running = True
        self.in_game = False  # สถานะเกมเริ่มต้น (ยังไม่ได้อยู่ในเกม)
        
    def game_screen(self):
        action = final_game.run_game()  # เรียกฟังก์ชันหลักของเกม
        if action == "game":
            return "game"
        if action == False:
            return False

    def main_menu(self):
        level = final_game.bestlvl
        self.screen.blit(self.bg_image, (0, 0))
        pygame.display.set_caption("FINAL ARROW")

        best_text = pygame.font.SysFont("Inter", 28).render(f"BEST LEVEL: {level}", True, "black")
        best_rect = best_text.get_rect(center=(540, 465))
        self.screen.blit(best_text, best_rect)

        # ปุ่ม START
        start_pic = pygame.image.load("button.png")
        start_button_surface = pygame.transform.scale(start_pic, (280, 200))
        start_button = Button(start_button_surface, 381, 550, "START")

        # ปุ่ม QUIT
        quit_pic = pygame.image.load("button.png")
        quit_button_surface = pygame.transform.scale(quit_pic, (280, 200))
        quit_button = Button(quit_button_surface, 699, 550, "QUIT")

        # ตรวจสอบการคลิก
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(pygame.mouse.get_pos()) == "game":
                    return "game"
                quit_button.checkForInput(pygame.mouse.get_pos())

        # อัปเดตการเปลี่ยนสีปุ่มเมื่อเมาส์ชี้อยู่
        start_button.changeColor(pygame.mouse.get_pos())
        quit_button.changeColor(pygame.mouse.get_pos())

        # วาดปุ่มบนหน้าจอ
        start_button.update()
        quit_button.update()

        pygame.display.update()

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def main(self): # ฟังก์ชันหลัก
        while self.running:
            if not self.in_game:
                self.in_game = self.main_menu()  # ถ้าไม่ได้อยู่ในเกม ให้แสดงหน้าหลัก
            else:
                self.in_game = self.game_screen()  # ถ้าอยู่ในเกม ให้ไปที่หน้าจอเกม

###########################################################################

if __name__ == "__main__":
    game = Game()
    game.main()  # เรียกใช้ฟังก์ชันหลักของเกม