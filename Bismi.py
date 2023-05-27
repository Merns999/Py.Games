import pygame , random , math, time

pygame.init()
screen = pygame.display.set_mode((800, 600))#setting the size of the screen

#writting a text on the screen
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

#condition for the running of the loop
running = True
# changing name and icon 
pygame.display.set_caption("Mansur")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# player
playerimg = pygame.image.load('fast.png')
playerX = 370
playerY = 480
def player(x,y):
    screen.blit(playerimg, (x ,y))
# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyNo = 6
for i in range(enemyNo):#placing the enemy details to every element in the enemy list
    enemyimg.append(pygame.image.load('space.png'))
    enemyX.append(random.randint(20, 600))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(0.3)
def enemy(x,y,i):#function for making the enemy appear on the screen
    screen.blit(enemyimg[i], (x,y))
# bullet
bulletimg = pygame.image.load('bullet.png')
bulletY = playerY
bulletX = 0
bullet_state = 'ready' #bullet cannot be seen in the screen
def bullet(x,y):#function for firing
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+13,y))
# function for collision
def collision(bulletX, bulletY,enemyX, enemyY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))# formular for collision
    if distance < 27:
        return True
    else:
        return False

down = 40
speed = 0.3
score = 0
Thescore = 10
WHITE = (255,255,255)

# infinite loop for running the game
while running:
    """makes sure the game is running always and the game doesnt close down"""
    screen.fill((105,105,105))#changing color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            """close functionallity"""
            running = False
    #checking whether a key is pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 0.7
            if playerX <= -1:
                playerX = 0
        if event.key == pygame.K_RIGHT:
            playerX += 0.7
            if playerX >= 750:
                playerX = 750
        if event.key == pygame.K_UP:
            if bullet_state == 'ready':
                bulletX = playerX
                bullet(bulletX, bulletY)
    # checking when the key is released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            # playerX += 10
            if playerX >= 750:
                playerX = 750
            if playerX <= -1:
                playerX = 0
    # moving the enemy accross y and x axis
    for i in range(enemyNo):
        enemyX[i] += enemyXchange[i]
        if score > Thescore:
            down = down + 40
            Thescore += 20
        if enemyX[i] >= 750:
            enemyXchange[i]  = -speed#speed = 0.3
            enemyY[i] += down #down = 40
        if enemyX[i] <= -1:
            enemyXchange[i] = speed
            enemyY[i] += down
        if enemyY[i] >= playerY:
            text_surface = my_font.render('You Lost', True, (0, 0, 0))
            screen.blit(text_surface, (400,300))
            pygame.time.wait(3000)
            # time.sleep(5)
            running = False #close functionality
        iscollision  = collision(bulletX,bulletY,enemyX[i],enemyY[i])
        if iscollision:
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            print(score)
            enemyX[i] = random.randint(20, 600)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
        

    if bulletY <= -20:
        bulletY = playerY
        bullet_state = 'ready'
    if bullet_state == 'fire':
        bullet(bulletX, bulletY)
        bulletY -= 1
    
    
    player(playerX, playerY)#calling the player functuin
    pygame.display.update()#updates the screen display, ie the game window 