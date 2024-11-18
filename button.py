import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1080,750))
main_font = pygame.font.SysFont("Inter",55)

class Button() :
    def __init__(self, image, x_pos, y_pos, text_input) :
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True , "white")
        self.text_rect = self.text. get_rect(center=(self.x_pos, self.y_pos))

    def update(self) :
        """อัปเดตการแสดงผลของปุ่ม"""
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position) :
        if self.rect.collidepoint(position) :

            if self.text_input == "QUIT": # อิงคำจากศัพท์บนปุ่ม
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
            
    def changeColor(self, position) :
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) :
            self.text = main_font.render(self.text_input, True , "red")
        else :
            self.text = main_font.render(self.text_input, True , "white")

        ''' position[0]: พิกัด x ของตำแหน่งเมาส์
            position[1]: พิกัด y ของตำแหน่งเมาส์
            self.rect.left: ขอบซ้ายของกรอบของปุ่ม
            self.rect.right: ขอบขวาของกรอบของปุ่ม
            self.rect.top: ขอบบนของกรอบของปุ่ม
            self.rect.bottom: ขอบล่างของกรอบของปุ่ม
            การใช้ range() ในที่นี้หมายถึงการสร้างช่วงค่าที่เราจะตรวจสอบ:

            range(self.rect.left, self.rect.right): สร้างช่วงค่าจากขอบซ้ายไปขอบขวาของกรอบ
            range(self.rect.top, self.rect.bottom): สร้างช่วงค่าจากขอบบนไปขอบล่างของกรอบ'''
