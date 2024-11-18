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
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((screen_w,screen_h))
#create screen window

pygame.display.set_caption("Pygame test program")
#set window name

clock = pygame.time.Clock()
#creat time for movement speed refernce
tick = 300

power = 0

class ARROW(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((4, 120))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hb = pygame.Rect(x,y-60,4,1)
    def update(self, dx=0):
        if self.rect.x > 910:
            self.rect.right = 910
        elif self.rect.x < 170:
            self.rect.left = 170
        else:
            self.rect.x += dx
            self.hb.x += dx

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
        self.y = y
        self.n = 0
        self.rect = pygame.Rect(self.x, self.y, 390, 120)
        self.hb = pygame.Rect(self.x,self.y+120,390,1)
        self.operation = random.choice(['+', '-', '*', '/'])
        self.color = green if self.operation in ['+', '*'] else red
        self.point = random.randint(1, 15) if self.operation in ['+', '-'] else random.randint(1, 3)

    def reset(self):
        self.y = -100
        self.hb.y = 20
        self.operation = random.choice(['+', '-', '*', '/'])
        self.color = green if self.operation in ['+', '*'] else red
        self.point = random.randint(1, 15) if self.operation in ['+', '-'] else random.randint(1, 3)

    def update(self):
        self.y += 1
        self.hb.y += 1
        if self.y > screen_h:
            self.reset()
            self.n += 1
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, white, self.hb)
        text = font.render(f'{self.operation}{self.point}', True, black)
        screen.blit(text, (self.x + 195 - (6 * len(f'{self.point}')), self.y + 55))
        
class Boss:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 120, 120)
        self.hb = pygame.Rect(x,self.rect.centery,120,1)

    def update(self):
        self.rect.y += 1
        self.hb.y += 1

    def draw(self):
        pygame.draw.rect(screen, blue, self.rect)
        pygame.draw.rect(screen, white, self.hb)
        
        text = font.render(f'{bosspower-50}', True, white)
        screen.blit(text, (self.rect.centerx- (6 * len(f'{bosspower-50}')), self.rect.centery))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((90, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image.fill(blue)
        self.effect = -1  # Increase arrows
        

def collision():
    global power
    global result
    global bosspower
    global enemy_group
    power1 = bosspower
    power2 = bosspower
    
    if arrow.hb.colliderect(square1.hb):
        if square1.operation == '+':
            power1 += square1.point
            power += square1.point
        elif square1.operation == '-':
            power1 -= square1.point
            power -= square1.point
        elif square1.operation == '*':
            power1 *= square1.point
            power *= square1.point
        elif square1.operation == '/':
            power1 //= square1.point
            power //= square1.point
        

    elif arrow.hb.colliderect(square2.hb):
        if square2.operation == '+':
            power2 += square2.point
            power += square2.point
        elif square2.operation == '-':
            power2 -= square2.point
            power -= square2.point
        elif square2.operation == '*':
            power2 *= square2.point
            power *= square2.point
        elif square2.operation == '/':
            power2 //= square2.point
            power //= square2.point
        
        
    elif arrow.hb.colliderect(boss.hb):
        result = power > bosspower-50

    for unit in enemy_group:
        if unit.rect.colliderect(arrow.hb):
            power -= 1
            enemy_group.remove(unit)

    bosspower += power1-bosspower if power1>power2 else power2-bosspower

def create_enemy():
        enemy = Enemy(random.randint(150,890),random.randint(-160,-40))
        enemy_group.append(enemy)



def run_game():
    global power, bosspower, result, arrow, square1, square2, enemy_group, boss
    arrow = ARROW(540, 520)
    roads = [Road(530,-60),Road(530,220),Road(530,480)]
    square1 = Square(150, -120)
    square2 = Square(540, -120)
    enemy_group = []
    boss = Boss(480, -120)

    power = 0
    bosspower = 0
    result = 'win'

    run = True
    while run:  # หรือ while run == True

        screen.fill(black)

        # อัปเดตและแสดงผลเกม
        for road in roads:
            road.update()
            road.draw()

        for unit in enemy_group:
            unit.rect.y += 1  # ย้ายศัตรูลง
            screen.blit(unit.image, unit.rect)

        pygame.draw.line(screen, white, (930, 0), (930, 750), 2)
        pygame.draw.line(screen, white, (148, 0), (148, 750), 2)

        dx = 0
        key = pygame.key.get_pressed()  # รับค่า input จากคีย์บอร์ด

        if square1.n < 5  and square2.n < 5:
            square1.draw()
            square1.update()
            square2.draw()
            square2.update()
            if random.randint(0, 500) == 1:
                create_enemy()
            if key[pygame.K_a] == True:
                dx = -2
            elif key[pygame.K_d] == True:
                dx = 2
            elif key[pygame.K_LEFT] == True:
                dx = -2
            elif key[pygame.K_RIGHT] == True:
                dx = 2
        else:
            square1.y = -140
            square2.y = -140
            boss.update()
            boss.draw()

            if arrow.rect.centerx > 540:
                arrow.rect.x = 540
                arrow.hb.centerx = 540
            elif arrow.rect.centerx < 540:
                arrow.rect.x = 540
                arrow.hb.centerx = 540

        arrow.update(dx)
        screen.blit(arrow.image, arrow.rect)

        for event in pygame.event.get():  # รับเหตุการณ์จากผู้ใช้
            if event.type == pygame.QUIT:  # ปิดหน้าต่างเกม
                run = False
        if key[pygame.K_ESCAPE] == True:
            run = False

        text = font.render(f'{power}', True, white)
        screen.blit(text, (arrow.rect.x - (6 * len(f'{power}')), arrow.rect.y + 150))

        collision()  # เรียกใช้ฟังก์ชันตรวจสอบการชน

        if result == True : 
            return win.win(screen) # เรียกหน้าจอ WIN

        if result == False :
            return lose.lose(screen)

        clock.tick(tick)  # ตั้งค่าเวลาให้กับเกม
        pygame.display.update()

    pygame.quit()