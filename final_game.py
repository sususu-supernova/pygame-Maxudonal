import pygame
import random
import win
import lose

pygame.init()

screen_w = 1080
screen_h = 750
#varible for screen window

white = (255,255,255)
black = (0,0,0)
green = (0,255,0,100)
red = (255,0,0,100)
blue = (0,0,255)

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((screen_w,screen_h))
#create screen window

pygame.display.set_caption("Pygame test program")
#set window name

clock = pygame.time.Clock()
#creat time for movement speed refernce
tick = 140

power = 0

class ARROW:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xb = x
        self.headx = x+1
        self.headxl = x-5
        self.headxr = x+6
        self.heady = y-5
        self.headyl = y
        self.headyr = y
        self.hb = pygame.Rect(self.x-1,self.heady,4,3)
        self.blt =[x-5,y+50]
        self.blb =[x-5,y+60]
        self.bmt =[x+1.5,y+40]
        self.bmb =[x+1.5,y+50]
        self.brt =[x+6.5,y+50]
        self.brb =[x+6.5,y+60]
    def update(self, dx=0):
        if 170>self.x+dx or self.x+dx> 910:
            pass
        else:
            self.x += dx
            self.xb += dx*1.18
            self.hb.x += dx
            self.headx += dx*0.985
            self.headxl += dx*1.005
            self.headxr += dx*1.005
            self.headyl += dx*0.009
            self.headyr -= dx*0.009
            self.blt[0] += dx*1.15
            self.blb[0] += dx*1.18
            self.bmt[0] += dx*1.13
            self.bmb[0] += dx*1.15
            self.brt[0] += dx*1.15
            self.brb[0] += dx*1.18
        self.hb = pygame.Rect(self.headx,self.heady,1,1)
    def draw(self):
        pygame.draw.line(screen, white,(self.x, self.y),(self.xb, self.y+60), 4)
        '''pygame.draw.rect(screen, white, self.hb)'''
        pygame.draw.polygon(screen,white,((self.headx,self.heady),(self.headxl,self.headyl),(self.headxr,self.headyr)))
        pygame.draw.polygon(screen,white,(self.bmt,self.brt,self.brb,self.bmb,self.blb,self.blt))

class Road:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 70)

    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_h:
            self.rect.y = -60

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

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
        '''pygame.draw.rect(screen, white, self.hb)'''
        text = font.render(f'{self.operation}{self.point}', True, white)
        screen.blit(text, (self.rect.centerx-(6*len(f'{self.point}')), self.rect.centery))
        pygame.draw.rect(screen,white, pygame.Rect(542.5-(self.w/50)/2,self.y,1+self.w/50,self.h))
        
class Boss:
    def __init__(self, x, y):
        self.size = 8
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.hb = pygame.Rect(self.rect.left,self.rect.centery,self.size,3)
        self.speed = 0

    def update(self):
        self.speed += 0.005
        self.size += 0.10 +self.speed/5
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.hb = pygame.Rect(self.rect.left-self.size/2,self.rect.centery,self.size,3)
        self.y += 0.30 +self.speed*(self.y/1000)
        self.hb.y += 0.30 +self.speed*(self.y/1000)
        self.rect.centerx = 540
        

    def draw(self):
        pygame.draw.rect(screen, blue, self.rect)
        '''pygame.draw.rect(screen, white, self.hb)'''

        
        text = font.render(f'{bosspower-50}', True, white)
        screen.blit(text, (self.rect.centerx- (6 * len(f'{bosspower-50}')), self.rect.centery))

class Enemy:
    def __init__(self, x, y):
        self.size = 1
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(blue)
        self.effect = -1
        self.speed = 0
        self.hb = pygame.Rect(self.rect.x,self.rect.centery,self.size,3)
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
        self.image.fill(blue)
        self.hb = pygame.Rect(self.rect.x,self.rect.centery,self.size,3)

    def draw(self):
        screen.blit(self.image, self.rect)
        '''pygame.draw.rect(screen, white, self.hb)'''

        

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
            
        if arrow.hb.colliderect(sq[0].hb):
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

        elif arrow.hb.colliderect(sq[1].hb):
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
            
    if arrow.hb.colliderect(boss.hb):
        result = power > bosspower-50

    for unit in enemy_group:
        if unit.hb.colliderect(arrow.hb):
            power -= 1
            enemy_group.remove(unit)


def create_enemy():
        global enemy_group
        enemy = Enemy(random.randint(520,560),270)
        enemy_group = [enemy] + enemy_group

arrow = ARROW(540,600)
roads = [Road(530,-60),Road(530,220),Road(530,480)]
square =[[Square(537, 270),Square(543, 270)]]
enemy_group = []
boss = Boss(540,270)
bosspower = 0
result = 'win'
n = 0
pastgate = 0

def run_game() :
        
        global arrow,roads,square,enemy_group,boss,bosspower,result,n,pastgate

        arrow = ARROW(540,600)
        roads = [Road(530,-60),Road(530,220),Road(530,480)]
        square =[[Square(537, 270),Square(543, 270)]]
        enemy_group = []
        boss = Boss(540,270)
        bosspower = 0
        result = 'win'
        n = 0
        pastgate = 0
    
        run = True

        while run:  #or while run == True

            screen.fill(black)
            #to refresh screen

            '''for road in roads:
                road.update()
                road.draw()'''

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
                dx = 0
            else:
                boss.update()
                boss.draw()

                if arrow.x in range(539,542):
                    arrow.x = 540 
                    arrow.xb = 540
                    arrow.hb.x = 540
                    arrow.headx = 540
                    arrow.headxl = 535
                    arrow.headxr = 545
                    arrow.heady = arrow.y-5
                    arrow.headyl = arrow.y
                    arrow.headyr = arrow.y
                    arrow.blt[0] = 535
                    arrow.blb[0] = 535
                    arrow.bmt[0] = 541
                    arrow.bmb[0] = 541
                    arrow.brt[0] = 546
                    arrow.brb[0] = 546
                    dx=0
                elif arrow.x < 539:
                    dx = 2
                elif arrow.x > 541:
                    dx = -2
                
            eventhandle()

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
            arrow.update(dx)
            arrow.draw()

            text = font.render(f'{power}', True, white)
            screen.blit(text, (arrow.x-(6*len(f'{power}')),arrow.y+100))

            if result == True:
                return win.win(screen)
            
            if result == False:
                return lose.lose(screen)
            
            clock.tick(tick) #set time tick
            pygame.display.flip()
            
        pygame.quit()