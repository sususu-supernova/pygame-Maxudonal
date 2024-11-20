import pygame
import random
import win
import lose

pygame.init()

bg_image = pygame.image.load("game_bg.png")

screen_w = 1080
screen_h = 750
#varible for screen window

white = (255,255,255)
black = (10,10,10)
green = (0,255,0,250)
red = (255,0,0,250)
blue = (0,0,255)
yellow = (255,255,0)
brown = (106,78,66)
sky = (135,206,235)
grass = (132,192,17)
dirt = (155,118,83)
#color variable

font = pygame.font.Font(None, 36)
#set font

screen = pygame.display.set_mode((screen_w,screen_h))
#create screen window

pygame.display.set_caption("Final Arrow")
#set window name

clock = pygame.time.Clock()
#creat time for movement speed refernce
tick = 130

#################################################################################

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
        pygame.draw.polygon(screen,self.color,((self.head[0],self.head[1]),(self.headl[0],self.headl[1]),(self.headr[0],self.headr[1])))
        pygame.draw.polygon(screen,black,((self.head[0],self.head[1]-1),(self.headl[0]-1,self.headl[1]+1),(self.headr[0]+1,self.headr[1]+1)),1)
        pygame.draw.line(screen, brown,(self.x, self.y),(self.xb, self.y+60), 4)
        pygame.draw.polygon(screen,self.color,(self.bmt,self.brt,self.brb,self.bmb,self.blb,self.blt))
        pygame.draw.polygon(screen,black,(self.bmt,self.brt,self.brb,self.bmb,self.blb,self.blt),1)

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

#################################################################################

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
        self.color = green if self.operation in ['+', '*'] else red
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
        screen.blit(self.image, self.rect)
        text = font.render(f'{self.operation}{self.point}', True, white)
        screen.blit(text, (self.rect.centerx-(6*len(f'{self.point}')), self.rect.centery))
        pygame.draw.rect(screen,white, pygame.Rect(542.5-(self.w/50)/2,self.y,1+self.w/50,self.h))

#################################################################################
        
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
        screen.blit(self.pic_surface, self.pic_rect)
        text = font.render(f'{bosspower-50}', True, black)
        screen.blit(text, (self.rect.centerx- (6 * len(f'{bosspower-50}')), self.rect.centery+40))

#################################################################################

class Enemy:
    def __init__(self, x, y, model):
        self.size = 10
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(blue)
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
        self.image.fill(blue)
        self.hb = pygame.Rect(self.rect.centerx-self.size/6,self.rect.centery,self.size/3,3)

    def draw(self):
        screen.blit(self.pic_surface, self.pic_rect)
        text = font.render('-1', True, black)
        screen.blit(text, ((self.rect.centerx-12), self.rect.centery-6))

#################################################################################

def eventhandle():
    global power
    global result
    global bosspower
    global enemy_group
    global pastgate
    power1 = bosspower
    power2 = bosspower
    
    for sq in square:
        if sq[0].rect.y > 750:
            square.remove(sq)
            pastgate += 1
            
        if arrows[0].hb.colliderect(sq[0].hb):
            if sq[0].operation == '+':
                power1 += sq[0].point
                power += sq[0].point
            elif sq[0].operation == '-':
                power1 -= sq[0].point
                power -= sq[0].point
            elif sq[0].operation == '*':
                power1 *= sq[0].point
                power *= sq[0].point
            elif sq[0].operation == '/':
                power1 //= sq[0].point
                power //= sq[0].point
            if sq[1].operation == '+':
                power2 += sq[1].point
            elif sq[1].operation == '-':
                power2 -= sq[1].point
            elif sq[1].operation == '*':
                power2 *= sq[1].point
            elif sq[1].operation == '/':
                power2 //= sq[1].point
        elif arrows[0].hb.colliderect(sq[1].hb):
            if sq[0].operation == '+':
                power1 += sq[0].point
            elif sq[0].operation == '-':
                power1 -= sq[0].point
            elif sq[0].operation == '*':
                power1 *= sq[0].point
            elif sq[0].operation == '/':
                power1 //= sq[0].point
            if sq[1].operation == '+':
                power2 += sq[1].point
                power += sq[1].point
            elif sq[1].operation == '-':
                power2 -= sq[1].point
                power -= sq[1].point
            elif sq[1].operation == '*':
                power2 *= sq[1].point
                power *= sq[1].point
            elif sq[1].operation == '/':
                power2 //= sq[1].point
                power //= sq[1].point
        
        if power1 >= power2:
            bosspower += (power1-bosspower)
        elif power2 > power1:
            bosspower += (power2-bosspower)
            
    if arrows[0].hb.colliderect(boss.hb):
        result = power > bosspower-50

    for unit in enemy_group:
        for arrow in arrows:
            if unit.hb.colliderect(arrow.hb):
                power -= 1
                enemy_group.remove(unit)
                break

#################################################################################

def create_enemy():
        global enemy_group
        model = random.choice(['enemy1.png','enemy2.png','enemy3.png'])
        enemy = Enemy(random.randint(520,560),270,model)
        enemy_group = [enemy] + enemy_group

#################################################################################

arrow = ARROW(540,600,yellow)
arrows = [arrow,]
square =[[Square(537, 270),Square(543, 270)]]
enemy_group = []
boss = Boss(540,270)
bosspower = 0
result = 'win'
n = 0
pastgate = 0
power = 0
level = 0
bestlvl = 0

#################################################################################

def run_game() :
        
        global arrows,square,enemy_group,boss,bosspower,result,n,pastgate,power,tick,level,bestlvl

        arrow = ARROW(540,600,yellow)
        arrows = [arrow,]
        square =[[Square(537, 270),Square(543, 270)]]
        enemy_group = []
        boss = Boss(540,270)
        bosspower = 0
        result = 'win'
        n = 0
        pastgate = 0
        power = 0

        run = True

        while run:  #or while run == True

            screen.blit(bg_image, (0, 0))
            pygame.draw.rect(screen, grass, pygame.Rect(0,270,1080,480))
            pygame.draw.polygon(screen, dirt, ((0,750),(535,270),(545,270),(1080,750)))
            #to refresh screen

            for unit in enemy_group:
                    unit.update()
                    unit.draw()
                    if unit.rect.y>750:
                        enemy_group.remove(unit)
            
            pygame.draw.line(screen,white,(0,750),(535,270),3)
            pygame.draw.line(screen,white,(545,270),(1080,750),3)
            pygame.draw.line(screen,white,(0,270),(1080,270),3)
            #draw street line parameter = (display, color, start, stop, width)
            key = pygame.key.get_pressed()  #get pressed key input
                
            eventhandle()

            dx = 0

            for event in pygame.event.get(): #get event input from user
                if event.type == pygame.QUIT: #to able to close game window
                    run = False
            if key[pygame.K_ESCAPE] == True:
                run = False
            if key[pygame.K_a] == True and pastgate < 11:
                dx = -3
            elif key[pygame.K_d] == True and pastgate < 11:
                dx = 3
            elif key[pygame.K_LEFT] == True and pastgate < 11:
                dx = -3
            elif key[pygame.K_RIGHT] == True and pastgate < 11:
                dx = 3
            
            if len(arrows) <= power //10:
                arrows.append(ARROW(random.randint(arrows[0].x-20,arrows[0].x+20),random.randint(605,610),white))
            if len(arrows) > (power //10)+1 and len(arrows) > 1:
                arrows.remove(arrows[-1])

            text = font.render(f'LEVEL : {level+1}', True, black)
            screen.blit(text, (510-(6*len(f'{level+1}')),10))

            if pastgate < 11:
                for sq in square:
                    if sq[0].rect.centery > 400 and len(square) == 1:
                        n+=1
                        if n < 11:
                            square.append([Square(537, 270),Square(543, 270)])
                    if random.randint(0,500) == 1 and n < 10:
                        create_enemy()
                    sq[0].draw()
                    sq[1].draw()
                    sq[0].update()
                    sq[1].update()
                for arrow in arrows[::-1]:
                    arrow.update(dx)
                    arrow.draw()
            else:
                boss.update()
                boss.draw()

                for arrow in arrows[::-1]:
                    arrow.center()
                    arrow.draw()

            text = font.render(f'{power}', True, white)
            screen.blit(text, (arrows[0].x-(6*len(f'{power}')),arrows[0].y+80))

            if result == True:
                tick += 10
                level += 1
                if level > bestlvl:
                    bestlvl = level
                return win.win(screen)
            
            if result == False:
                tick = 140
                level = 0
                return lose.lose(screen)
            
            clock.tick(tick) #set time tick
            pygame.display.flip()
            
        pygame.quit()