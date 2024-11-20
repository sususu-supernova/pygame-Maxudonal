import pygame
import random

import win
import lose
import setting

from arrow import ARROW
from square import Square
from boss import Boss
from enemy import Enemy

pygame.init()

pygame.display.set_caption("Final Arrow")
#set window name

arrow = ARROW(540,600,setting.yellow)
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
    pygame.draw.rect(setting.screen,setting.white,arrows[0].hb)

####

#################################################################################

def create_enemy():
        global enemy_group
        model = random.choice(['enemy1.png','enemy2.png','enemy3.png'])
        enemy = Enemy(random.randint(520,560),270,model)
        enemy_group = [enemy] + enemy_group

#################################################################################

def run_game() :
        
        global arrow,square,enemy_group,boss,bosspower,result,n,pastgate,power,level,bestlvl,arrows

        arrow = ARROW(540,600,setting.yellow)
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

            setting.screen.blit(setting.game_bg_image, (0, 0))
            pygame.draw.rect(setting.screen, setting.grass, pygame.Rect(0,270,1080,480))
            pygame.draw.polygon(setting.screen, setting.dirt, ((0,750),(535,270),(545,270),(1080,750)))
            #to refresh screen

            for unit in enemy_group:
                    unit.update()
                    unit.draw()
                    if unit.rect.y>750:
                        enemy_group.remove(unit)
            
            pygame.draw.line(setting.screen,setting.white,(0,750),(535,270),3)
            pygame.draw.line(setting.screen,setting.white,(545,270),(1080,750),3)
            pygame.draw.line(setting.screen,setting.white,(0,270),(1080,270),3)
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
                arrows.append(ARROW(random.randint(arrows[0].x-20,arrows[0].x+20),random.randint(605,610),setting.white))
            if len(arrows) > (power //10)+1 and len(arrows) > 1:
                arrows.remove(arrows[-1])

            text = setting.font.render(f'LEVEL : {level+1}', True, setting.black)
            setting.screen.blit(text, (510-(6*len(f'{level+1}')),10))

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

            text = setting.font.render(f'{power}', True, setting.white)
            setting.screen.blit(text, (arrows[0].x-(6*len(f'{power}')),arrows[0].y+80))

            if result == True:
                setting.tick += 10
                level += 1
                if level > bestlvl:
                    bestlvl = level
                return win.win(setting.screen)
            
            if result == False:
                setting.tick = 140
                level = 0
                return lose.lose(setting.screen)
            
            setting.clock.tick(setting.tick) #set time tick
            pygame.display.flip()
            
        pygame.quit()