import pygame
import sys
import os
from time import sleep
from math import asin, acos, sin, cos, pi, sqrt, hypot
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
collision = pygame.Surface((800,600), pygame.SRCALPHA)
collision.fill((255,255,255,128))

class Character:

    def __init__(self):

        self.leftCounter = 0
        self.rightCounter = 0
        self.upCounter = 0
        self.downCounter = 0
        self.lastDirection = "down"
        self.characterSprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

    #def __init__(self, hp, mp, deff, vit, wis, dex, att, spd):
    #    self.hp = hp;
    #    self.mp = mp;
    #    self.deff = deff;
    #    self.vit = vit;
    #    self.wis = wis;
    #    self.dex = dex;
    #    self.att = att;
    #    self.spd = spd;

    def leftWalk(self):

        self.lastDirection = "left"
        self.leftCounter += 1

        if self.leftCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()
            
        elif self.leftCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherWalkLeft2.png").convert_alpha()
            
        else:
            
            self.leftCounter = 0

    def rightWalk(self):

        self.lastDirection = "right"
        self.rightCounter += 1
        
        if self.rightCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()
            
        elif self.rightCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherWalkRight2.png").convert_alpha()
            
        else:
            
            self.rightCounter = 0

    def upWalk(self):

        self.lastDirection = "up"
        self.upCounter += 1
        
        if self.upCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherWalkUp1.png").convert_alpha()
            
        elif self.upCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherWalkUp2.png").convert_alpha()
            
        else:
            
            self.upCounter = 0

    def downWalk(self):

        self.lastDirection = "down"
        self.downCounter += 1
        
        if self.downCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherWalkDown1.png").convert_alpha()
            
        elif self.downCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherWalkDown2.png").convert_alpha()
            
        else:
            
            self.downCounter = 0
            
    def leftShoot(self):

        self.lastDirection = "left"
        self.leftCounter += 1
        
        if self.leftCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherShootLeft1.png").convert_alpha()
            
        elif self.leftCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherShootLeft2.png").convert_alpha()
            
        else:
            
            self.leftCounter = 0

    def rightShoot(self):

        self.lastDirection = "right"

        self.rightCounter += 1
        
        if self.rightCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherShootRight1.png").convert_alpha()
            
        elif self.rightCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherShootRight2.png").convert_alpha()
            
        else:
            
            self.rightCounter = 0

    def upShoot(self):

        self.lastDirection = "up"
        self.upCounter += 1

        if self.upCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherShootUp1.png").convert_alpha()
            
        elif self.upCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherShootUp2.png").convert_alpha()
            
        else:
            
            self.upCounter = 0

    def downShoot(self):

        self.lastDirection = "down"
        self.downCounter += 1
        
        if self.downCounter < 10:
            
            self.characterSprite = pygame.image.load("ArcherShootDown1.png").convert_alpha()
            
        elif self.downCounter < 20:
            
            self.characterSprite = pygame.image.load("ArcherShootDown2.png").convert_alpha()
            
        else:
            
            self.downCounter = 0

    def release(self):
        
        self.leftCounter = 0
        self.rightCounter = 0
        self.downCounter = 0
        self.upCounter = 0

        if self.lastDirection == "left":

            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()

        elif self.lastDirection == "right":

            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

        elif self.lastDirection == "up":

            self.characterSprite = pygame.image.load("ArcherNeutralUp.png").convert_alpha()

        elif self.lastDirection == "down":

            self.characterSprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

class Projectile():

    def __init__(self, angle, lifespan, x, y, xOffset, yOffset):

        self.angle    = angle
        self.lifespan = lifespan
        self.x        = x
        self.y        = y
        self.xOffset  = xOffset
        self.yOffset  = yOffset

red          = (255,  0,  0)
green        = (  0,255,  0)
blue         = (  0,  0,255)
white        = (255,255,255)
black        = (  0, 0,  0)
grey         = (127,127,127)

tileList    = [black, white, grey, red, green, blue]

sidebar      = [600, 0, 200, 800]
healthbar    = [610, 150, 180, 20]
character    = Character()
characterXY  = [275, 275]
characterXYHitbox  = [275, 275, 50, 50]
enemyXY = [100, 100]
enemyXYHitbox = [100, 100, 100, 100]

enemyXOffset = 0
enemyYOffset = 0

tileLength   = 50

centerX      = 300
centerY      = 300

frame        = 0
shotDelay    = 15
lastClick    = -60

projectileList  = []

enemySprite1 = pygame.image.load("Occulusion1.PNG").convert_alpha()
enemySprite2 = pygame.image.load("Occulusion2.PNG").convert_alpha()
enemySprite3 = pygame.image.load("Occulusion3.PNG").convert_alpha()
currentEnemySprite = enemySprite1
projectileSprite = pygame.image.load("Arrow.PNG").convert_alpha()

map_ = open("ROTMG_Map.txt", "r")
mapList = [line.rstrip('\n') for line in map_]
map_.close()

for i in range(0, len(mapList)):

    mapList[i] = list(mapList[i])

mapWidth  = len(mapList) * tileLength
mapHeight = len(mapList[0]) * tileLength

xPos = (mapWidth) / 2
yPos = (mapHeight) / 2

ended = False

step = 0

while not ended:

    screen.fill(black)
    collision.fill(white)

    for x in range(-6,7):

        for y in range(-6,7):

            if (xPos / 50) + x < 0 or (yPos / 50) + y < 0:

                pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

            else:

                try:

                    pygame.draw.rect(screen, tileList[int(mapList[(int(xPos) / 50) + x][(int(yPos) / 50) + y])], (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

                except IndexError:

                    pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

    keyDown = pygame.key.get_pressed()
        
    if keyDown[pygame.K_w]:

        yPos = max(0, yPos - 5)

        if yPos <= 0:

            enemyYOffset = 0

        else:

            for i in projectileList:
                
                i.yOffset = i.yOffset - 5

            enemyYOffset -= 5
            
    if keyDown[pygame.K_s]:

        yPos = min(mapHeight, yPos + 5)

        if yPos >= len(mapList[0]) * 50:

            enemyYOffset = 0

        else:

            for i in projectileList:
                    
                i.yOffset = i.yOffset + 5

            enemyYOffset += 5
            
    if keyDown[pygame.K_a]:

        xPos = max(0, xPos - 5)

        if xPos <= 0:

            enemyXOffset = 0

        else:

            for i in projectileList:
                    
                i.xOffset = i.xOffset - 5

            enemyXOffset -= 5

    if keyDown[pygame.K_d]:

        xPos = min(mapWidth, xPos + 5)

        if xPos >= len(mapList) * 50:

            enemyXOffset = 0

        else:

            for i in projectileList:
                    
                i.xOffset = i.xOffset + 5

            enemyXOffset += 5
    
    if keyDown[pygame.K_SPACE]:

        pass

    if pygame.mouse.get_pressed()[0]:

        mouseX, mouseY = pygame.mouse.get_pos()

        if frame >= lastClick + shotDelay:

            lastClick = frame

            xLength = centerX - mouseX
            yLength = centerY - mouseY
            distance = hypot(xLength, yLength)

            try:

                angle = acos(xLength / distance)

            except ZeroDivisionError:

                angle = 0

            if yLength < 0:

                angle = 2 * pi - angle

            lifespan = 30

            x = 300
            y = 300
            xOffset = 0
            yOffset = 0

            projectile = Projectile(angle, lifespan, x, y, xOffset, yOffset)

            projectileList.append(projectile)

    for i in projectileList:

        hitbox = pygame.Rect(i.x, i.y, 5, 5)

        if hitbox.colliderect(enemyXYHitbox) == True:

            projectileList.remove(i)

        else:

            if i.lifespan <= 25:
            
                screen.blit(pygame.transform.rotate(projectileSprite, (i.angle - 3 * pi/4) * (-180/pi)), (int(i.x - 30), int(i.y - 30)))

            pygame.draw.rect(collision, red, (int(i.x), int(i.y), 5, 5))

            i.x -= 10 * cos(i.angle) + i.xOffset
            i.y -= 10 * sin(i.angle) + i.yOffset
            i.xOffset = 0
            i.yOffset = 0

            i.lifespan -= 1

            if i.lifespan <= 0:

                projectileList.remove(i)
            
    if pygame.mouse.get_pressed()[0]:

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseY - 300 >= abs(mouseX - 300):

            character.downShoot()

        elif mouseX - 300 >= abs(mouseY - 300):

            character.rightShoot()

        elif -mouseY + 300 >= abs(mouseX - 300):

            character.upShoot()

        elif -mouseX + 300 >= abs(mouseY - 300):

            character.leftShoot()

    elif keyDown[pygame.K_w] and keyDown[pygame.K_s]:

        character.release()

    elif keyDown[pygame.K_a] and keyDown[pygame.K_d]:

        character.release()

    elif keyDown[pygame.K_a]:

        character.leftWalk()

    elif keyDown[pygame.K_d]:

        character.rightWalk()

    elif keyDown[pygame.K_w]:

        character.upWalk()

    elif keyDown[pygame.K_s]:

        character.downWalk()

    else:

        character.release()

    if frame % 60 == 0:

        currentEnemySprite = enemySprite1

    elif frame % 60 == 15:

        currentEnemySprite = enemySprite2

    elif frame % 60 == 30:

        currentEnemySprite = enemySprite3

    elif frame % 60 == 45:

        currentEnemySprite = enemySprite2

    enemyXY[0] -= enemyXOffset
    enemyXY[1] -= enemyYOffset
    enemyXYHitbox[0] -= enemyXOffset
    enemyXYHitbox[1] -= enemyYOffset

    enemyXOffset = 0
    enemyYOffset = 0
    
    screen.blit(character.characterSprite, characterXY)
    screen.blit(currentEnemySprite, enemyXY)
    pygame.draw.rect(screen, grey, sidebar)
    pygame.draw.rect(screen, red, healthbar)
    pygame.draw.rect(collision, grey, characterXYHitbox)
    pygame.draw.rect(collision, grey, enemyXYHitbox)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            ended = True

    pygame.display.flip()

    sleep(1.0/60)

    frame += 1

    print xPos

pygame.quit()
