import pygame
import setting
import random

pygame.init()

class Square:
    def __init__(self, x, y):
        self.x = x
        self.xf = x
        self.y = y
        self.yf = y
        self.w = 5
        self.h = 2
        self.speed = 0
        self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.hb = pygame.Rect(self.x,self.y+self.h,self.w,2)
        self.operation = random.choice(['+', '-', '*', '/'])
        self.color = setting.green if self.operation in ['+', '*'] else setting.red
        self.point = random.randint(1, 15) if self.operation in ['+', '-'] else random.randint(1, 3)
        self.image.fill(self.color)

    def update(self):
        self.speed += 0.005
        self.y += 0.20 +self.speed*(self.y/950)
        self.w += 0.56 +self.speed*(self.y/950)
        self.h += 0.20 +self.speed/3
        self.hb.y = self.rect.centery
        self.hb.width = self.w
        if self.x < 540:
            self.x -= 0.56 +self.speed*(self.y/950)
            self.hb.x = self.x
        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(self.color)

    def draw(self):
        pygame.Surface.set_alpha(self.image,150)
        setting.screen.blit(self.image, self.rect)
        text = setting.font.render(f'{self.operation}{self.point}', True, setting.white)
        setting.screen.blit(text, (self.rect.centerx-(6*len(f'{self.point}')), self.rect.centery))
        pygame.draw.rect(setting.screen,setting.white, pygame.Rect(542.5-(self.w/50)/2,self.y,1+self.w/50,self.h))