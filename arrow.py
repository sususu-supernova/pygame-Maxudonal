import pygame
import setting

pygame.init()

class ARROW:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.xb = ((x-540)*1.18)+540
        self.head = [(self.x-540)*0.985+1+540,y-5]
        self.headl = [(self.x-540)*1.005-5+540,y]
        self.headr = [(self.x-540)*1.005+6+540,y]
        self.hb = pygame.Rect(self.x-1,self.head[1],1,1)
        self.blt =[((self.x-540)*1.15)-5+540,self.y+50]
        self.blb =[((self.x-540)*1.18)-5+540,self.y+60]
        self.bmt =[((self.x-540)*1.13)+1.5+540,self.y+40]
        self.bmb =[((self.x-540)*1.15)+1.5+540,self.y+50]
        self.brt =[((self.x-540)*1.15)+6.5+540,self.y+50]
        self.brb =[((self.x-540)*1.18)+6.5+540,self.y+60]

    def update(self, dx):
        if 170>self.x+dx or self.x+dx> 910:
            pass
        else:
            self.x += dx
            self.xb += dx*1.18
            self.hb.x += dx
            self.head[0] += dx*0.985
            self.headl[0] += dx*1.005
            self.headr[0] += dx*1.005
            self.headl[1] += dx*0.009
            self.headr[1] -= dx*0.009
            self.blt[0] += dx*1.15
            self.blb[0] += dx*1.18
            self.bmt[0] += dx*1.13
            self.bmb[0] += dx*1.15
            self.brt[0] += dx*1.15
            self.brb[0] += dx*1.18
        self.hb = pygame.Rect(self.head[0],self.head[1],1,1)

    def draw(self):
        pygame.draw.polygon(setting.screen,self.color,((self.head[0],self.head[1]),(self.headl[0],self.headl[1]),(self.headr[0],self.headr[1])))
        pygame.draw.polygon(setting.screen,setting.black,((self.head[0],self.head[1]-1),(self.headl[0]-1,self.headl[1]+1),(self.headr[0]+1,self.headr[1]+1)),1)
        pygame.draw.line(setting.screen, setting.brown,(self.x, self.y),(self.xb, self.y+60), 4)
        pygame.draw.polygon(setting.screen,self.color,(self.bmt,self.brt,self.brb,self.bmb,self.blb,self.blt))
        pygame.draw.polygon(setting.screen,setting.black,(self.bmt,self.brt,self.brb,self.bmb,self.blb,self.blt),1)

    def center(self):
        if self.x in range(539,542):
            self.x = 540 
            self.xb = 540
            self.hb.x = 540
            self.head[0] = 540 
            self.headl[0] = 535
            self.headr[0] = 545
            self.head[1] = self.y-5
            self.headl[1] = self.y
            self.headr[1] = self.y
            self.blt[0] = 535
            self.blb[0] = 535
            self.bmt[0] = 541
            self.bmb[0] = 541
            self.brt[0] = 546
            self.brb[0] = 546
            dx=0
            self.update(dx)
        elif self.x < 539:
            dx = 2
            self.update(dx)
        elif self.x > 541:
            dx = -2
            self.update(dx)