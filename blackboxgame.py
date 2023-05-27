import pygame, math
pygame.init()

screen = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()
FPS =  50 

count = 0
rectx = 100
recty = 50

RECTCLOLOR = (227, 83, 53)

# for i in range(11):
#     pygame.draw.rect(screen,(227, 83, 53),(200,10,(rectx + 10 * i),recty))

def collision(rectX, rectY, ballX, ballY):
    distance = math.sqrt(math.pow((rectX - ballX), 2) + math.pow((rectY- ballY), 2))
    if distance < 27:
        return True
    else:
        return False
class Ball():
    def __init__(self):
        self.y= 200
        self.x = 0
        self.velocityy =  6
        self.velocityx = 6
    def draw(self):
        pygame.draw.circle(screen, (0,255,0),(self.x, int(self.y)),10)
    def move(self):
        # self.velocityy += Acc
        self.y += self.velocityy
        self.x += self.velocityx
        # if self.y >= 340:
        #     self.velocityy = 0
        #     self.velocityx = 0
        if self.y >= 340 or self.y <= 0:
            self.velocityy = -self.velocityy
        if self.x >= 500 or self.x <= 0:
            self.velocityx = -self.velocityx
    
def draw_rect():
    pygame.draw.rect(screen,(227, 83, 53),(200,10,rectx,recty))
    


def game():
    ball = Ball()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ball.move()
        screen.fill((70 , 130, 180))
        pygame.draw.line(screen, (0,0,0),(0,350),(700,350), 5)
        
        ball.draw()
        draw_rect()
        iscollision = collision(draw_rect.rectx, draw_rect.recty, ball.x, ball.y)
        if iscollision:
            print("touched")
        else:
            draw_rect()
        pygame.display.update()
        clock.tick(FPS)
game()
pygame.quit()
