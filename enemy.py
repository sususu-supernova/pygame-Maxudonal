import pygame
import setting

pygame.init()

class Enemy:
    def __init__(self, x, y, model):
        self.size = 10
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(setting.blue)
        self.effect = -1
        self.speed = 0
        self.hb = pygame.Rect(self.rect.centerx-self.size/6,self.rect.centery,self.size/3,3)
        self.pic = pygame.image.load(model)
        self.pic_surface = pygame.transform.scale(self.pic, (self.size, self.size*1.5))
        self.pic_rect = self.image.get_rect()
        self.pic_rect = (self.rect.x,self.y-self.size/2.5)

    def update(self):
        self.speed += 0.005
        self.y += 0.30 +self.speed*(self.y/1000)
        self.size += 0.10 +self.speed/5
        if self.rect.centerx < 540:
            self.x -= (540-self.rect.centerx)/170
        elif self.rect.centerx > 540:
            self.x += (self.rect.centerx-540)/170
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.y = self.y
        self.pic_rect = (self.rect.x,self.y-self.size/2.5)
        self.pic_surface = pygame.transform.scale(self.pic, (self.size, self.size*1.5))
        self.image.fill(setting.blue)
        self.hb = pygame.Rect(self.rect.centerx-self.size/6,self.rect.centery,self.size/3,3)

    def draw(self):
        setting.screen.blit(self.pic_surface, self.pic_rect)
        text = setting.font.render('-1', True, setting.black)
        setting.screen.blit(text, ((self.rect.centerx-12), self.rect.centery-6))
