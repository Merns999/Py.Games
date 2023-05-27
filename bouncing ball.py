# bouncing ball

import pygame, random

pygame.init()
screen = pygame.display.set_mode([700,500])#setting the size of the screen
clock = pygame.time.Clock()#pauses program

# Set up global variables
class Ball():
    x = y = xspeed = yspeed = colour = rad = 0#initializing every variable to 0
class rec():
    x = y = w = h = colour = 0
w = screen.get_width()#sets w to size of the width of the screen
h = screen.get_height()#sets h to the size of the height of the screen

rect_list = [pygame.Rect(w//4, h//4, w//7, h //5), pygame.Rect(w*3//4, h*3//4, w//7, h //5)] #list of two rectangles settiin its left, top, width and height valus

# Create a list of balls
balls = []

# Create ball and include in the list of balls
for i in range(1):
    ball = Ball()
    ball.x = random.randint(0,w-ball.rad-ball.rad)
    ball.y = random.randint(0,h-ball.rad-ball.rad)
    ball.xspeed = random.randint(-2,2)
    ball.yspeed = random.randint(-2,2)
    while ball.xspeed == 0 or ball.yspeed == 0:#resets the ball speed to range between the numbers -2, 2
        ball.xspeed = random.randint(-2,2)
        ball.yspeed = random.randint(-2,2)
    ball.rad = random.randint(5,30)
    ball.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if ball.x + ball.rad <= w and ball.y + ball.rad <= h:
        balls.append(ball)
#Game loop
while True:
    # ===================== HANDLE EVENTS (DO NOT EDIT) ===================== #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

    if done == True:
        break
    # ============================== MOVE STUFF ============================= #
    for ball in balls:
        ball.x = ball.x + ball.xspeed
        ball.y = ball.y + ball.yspeed
    # ============================== COLLISION ============================== #
    for ball in balls:
        if ball.x - ball.rad <= 0:
            ball.xspeed = abs(ball.xspeed)
        elif ball.x + ball.rad >= w:
            ball.xspeed = -abs(ball.xspeed)
        if ball.y - ball.rad<= 0 :
            ball.yspeed = abs(ball.yspeed)
        elif ball.y + ball.rad >= h:
            ball.yspeed = -abs(ball.yspeed)

        for rect in rect_list:
            ball_rect = pygame.Rect((0,0), (ball.rad*2, ball.rad*2))
            ball_rect.center = int(ball.x),int(ball.y)
            if rect.colliderect(ball_rect):
                v = pygame.math.Vector2(ball.xspeed, ball.yspeed)
                dx = ball.x - rect.centerx
                dy = ball.y - rect.centery
                if abs(dx) > abs(dy):
                    ball.x = rect.left-ball.rad if dx < 0 else rect.right+ball.rad
                    if (dx < 0 and v[0] > 0) or (dx > 0 and v[0] < 0):
                        v.reflect_ip(pygame.math.Vector2(1, 0))
                else:
                    ballposy = rect.top-ball.rad if dy < 0 else rect.bottom+ball.rad
                    if (dy < 0 and v[1] > 0) or (dy > 0 and v[1] < 0):
                        v.reflect_ip(pygame.math.Vector2(0, 1))
                ball.xspeed, ball.yspeed = v.x, v.y

    # ============================== DRAW STUFF ============================= #                               
    screen.fill ((255,255,255))
    for ball in balls:
        pygame.draw.circle (screen, (ball.colour), (ball.x,ball.y), ball.rad)
    for rect in rect_list:
        pygame.draw.rect(screen, (0,255,0), rect)
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    clock.tick(100)