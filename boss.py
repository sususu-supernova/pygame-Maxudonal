import pygame
import setting
import final_game

pygame.init()

class Boss:
    def __init__(self, x, y):
        self.size = 16
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.hb = pygame.Rect(self.rect.left,self.rect.centery,self.size,3)
        self.speed = 0
        self.pic = pygame.image.load('boss.png')
        self.pic_surface = pygame.transform.scale(self.pic, (self.size*1.2, self.size))
        self.pic_rect = self.pic.get_rect()
        self.pic_rect = (self.rect.x-self.size/8,self.y-10)


    def update(self):
        self.speed += 0.003
        self.size += 0.50 +self.speed/5
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.hb = pygame.Rect(self.rect.left-self.size/2,self.rect.centery,self.size,3)
        self.y += 0.30 +self.speed*(self.y/1000)
        self.hb.y += 0.30 +self.speed*(self.y/1000)
        self.rect.centerx = 540
        self.pic_rect = (self.rect.x-self.size/8,self.y-10)
        self.pic_surface = pygame.transform.scale(self.pic, (self.size*1.2, self.size))
        
    def draw(self):
        setting.screen.blit(self.pic_surface, self.pic_rect)
        text = setting.font.render(f'{final_game.bosspower-50}', True, setting.black)
        setting.screen.blit(text, (self.rect.centerx- (6 * len(f'{final_game.bosspower-50}')), self.rect.centery+40))
