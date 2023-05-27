#bouncing ball game using pygame
import pygame, time, random, math
from pygame.locals import*
#settint the screen size and appearance
pygame.init()
pygame.display.set_caption("Bouncing Balls")
bgcolour = (8.24, 13.3, 22)
w, h = 640, 480
screen = pygame.display.set_mode((w, h))
screen.fill((bgcolour))

#ball
ballimg = pygame.image.load('/home/mernsur/Documents/ppytrials/ball.png')
ballX, ballY = 310,450
def ballpos(x,y):#settting the ball position
    screen.blit(ballimg,(x+10,y+10))

#boxes 
boximg = []
boxNo=10
space = 38
boxX, boxY1, boxY2, boxY3  = [], [], [], []
for j in range(3):
    for i in range(boxNo):
        boximg.append(pygame.image.load('/home/mernsur/Documents/ppytrials/balls/green48.png'))
        boxX.append(70 + i* space)
        boxY1.append(j)
        def boxpos1(x,y):
            screen.blit(boximg[i], (x,y))

for i in range(boxNo):
    boximg.append(pygame.image.load('/home/mernsur/Documents/ppytrials/balls/green48.png'))
    boxX.append(70 + i* space)
    boxY1.append(10)
    def boxpos1(x,y):
        screen.blit(boximg[i], (x,y))
for i in range(boxNo):
    boximg.append(pygame.image.load('/home/mernsur/Documents/ppytrials/balls/green48.png'))
    boxX.append(70 + i* space)
    boxY2.append(50)
    def boxpos2(x,y):
        screen.blit(boximg[i], (x,y))
for i in range(boxNo):
    boximg.append(pygame.image.load('/home/mernsur/Documents/ppytrials/balls/green48.png'))
    boxX.append(70 + i* space)
    boxY3.append(90)
    def boxpos3(x,y):
        screen.blit(boximg[i], (x,y))


#movement
dx = dy = mouseX = mouseY = stepx = stepy = score = 0
side = ""

def collison(ballx, bally, boxx, boxy):
    distance = math.sqrt(math.pow((ballx - boxx), 2) + math.pow((bally - boxy), 2))# formular for collision
    if distance < 27:
        return True
    else:
        return False
        
#condition for running the main loop
running = True
touchBox = True

while running:
    screen.fill((bgcolour))
    for box in range(boxNo):
        boxpos1(boxX[box], boxY1[box])
    for box in range(boxNo):
        boxpos2(boxX[box], boxY2[box])
    for box in range(boxNo):
        boxpos3(boxX[box], boxY3[box])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ballpos(310,450)
                print("Return to original")
        if event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()#gets the position of where the mouse is clicked
            print(mouseX, mouseY)
            dx, dy = (mouseX - ballX, mouseY - ballY)
            stepx, stepy = (dx / 100., dy / 100.)
    if ballX != mouseX and ballY != mouseY:
        ballX, ballY = ballX+stepx, ballY+stepy
            
        if ballX >= 620:
            stepx = -abs(stepx)
        if ballX <= -10:
            stepx = abs(stepx)
        if ballY >=480 :
            stepy = -abs(stepy) 
        if ballY <= -10:
            stepy = abs(stepy)

    for i in range(3):
        
        for box in range(boxNo):
            collided = collison(ballX, ballY, boxX[box],boxY1[box])
            
            if ballY < (boxY1[box] + 10) and  ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
                stepx = - abs(stepx)
            if ballY > (boxY1[box] + 10) and ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
                stepx = abs(stepx)
            if ballX > (boxX[box] + 10) and ballY < (boxY1[box] +10 ) and ballY > (boxY1[box] - 10) :
                stepy = abs(stepy)
            if ballX < (boxX[box] + 10) and ballY < (boxY1[box] +10 ) and ballY > (boxY1[box] - 10) :
                stepy = -abs(stepy)
                if ballX > boxX[box]:
                    stepx = abs(stepx)
                if ballY > boxY1[box]:
                    stepy = abs(stepy)
                if ballX < boxX[box]:
                    stepx =  -abs(stepx)
                if ballY < boxY1[box]:
                    stepy = -abs(stepy)
                score += 1
                print(score)
    for box in range(boxNo):
        collided = collison(ballX, ballY, boxX[box],boxY1[box])
        if collided:
            # if ballY < (boxY1[box] + 10) and  ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = - abs(stepx)
            # if ballY > (boxY1[box] + 10) and ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = abs(stepx)
            # if ballX > (boxX[box] + 10) and ballY < (boxY1[box] +10 ) and ballY > (boxY1[box] - 10) :
            #     stepy = abs(stepy)
            # if ballX < (boxX[box] + 10) and ballY < (boxY1[box] +10 ) and ballY > (boxY1[box] - 10) :
            #     stepy = -abs(stepy)
            if ballX > boxX[box]:
                stepx = abs(stepx)
            if ballY > boxY1[box]:
                stepy = abs(stepy)
            if ballX < boxX[box]:
                stepx =  -abs(stepx)
            if ballY < boxY1[box]:
                stepy = -abs(stepy)
            score += 1
            print(score)
    for box in range(boxNo):
        collided = collison(ballX, ballY, boxX[box],boxY2[box])
        if collided:
            # if ballY < (boxY2[box] + 10) and  ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = - abs(stepx)
            # if ballY > (boxY2[box] + 10) and ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = abs(stepx)
            # if ballX > (boxX[box] + 10) and ballY < boxY2[box] +10 and ballY > boxY2[box] - 10 :
            #     stepy = abs(stepy)
            # if ballX < (boxX[box] + 10) and ballY < boxY2[box] +10 and ballY > boxY2[box] - 10 :
            #     stepy = -abs(stepy)
            if ballX > boxX[box]:
                stepx = abs(stepx)
            if ballY > boxY2[box]:
                stepy = abs(stepy)
            if ballX < boxX[box]:
                stepx =  -abs(stepx)
            if ballY < boxY2[box]:
                stepy = -abs(stepy)
            score += 1
            print(score)
    for box in range(boxNo):
        collided = collison(ballX, ballY, boxX[box],boxY3[box])
        if collided:
            # if ballY < (boxY3[box] + 10) and  ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = - abs(stepx)
            # if ballY > (boxY3[box] + 10) and ballX < (boxX[box] + 10) and ballX > (boxX[box] - 10):
            #     stepx = abs(stepx)
            # if ballX > (boxX[box] + 10) and ballY < (boxY3[box] +10) and ballY > (boxY3[box] - 10):
            #     stepy = abs(stepy)
            # if ballX < (boxX[box] + 10) and ballY < (boxY3[box] +10) and ballY > (boxY3[box] - 10):
            #     stepy = -abs(stepy)
            if ballX > boxX[box]:
                stepx = abs(stepx)
            if ballY > boxY3[box]:
                stepy = abs(stepy)
            if ballX < boxX[box]:
                stepx =  -abs(stepx)
            if ballY < boxY3[box]:
                stepy = -abs(stepy)
            score += 1
            print(score)
    

    ballpos(ballX, ballY)
    pygame.display.update()#updating the loop every time
