import pygame
from random import randint
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
class Paddle(pygame.sprite.Sprite):#paddle class: derived from "Sprite" class in python
    def __init__(self, color, width, height):# Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])#setting the screen 
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])#paddle
 
        self.rect = self.image.get_rect()# Fetch the rectangle object that has the dimensions of the image.
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
	    #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
 
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:
          self.rect.x = 700

class Ball(pygame.sprite.Sprite):# all. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]     
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

class Brick(pygame.sprite.Sprite):#Brick class. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
pygame.init()

score = 0
lives = 5
#Set window size
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BrickGame")

all_sprites_list = pygame.sprite.Group()#list containing all the sprites used in the game
 
#Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 345#setting the balls x coordinate
ball.rect.y = 195#setting the balls y coordinate
 
all_bricks = pygame.sprite.Group()
#placing the bricks in place
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100#setting the first set of bricks x coordinate
    brick.rect.y = 60#setting the top most row of bricks Y coordinate
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100#setting the second row of bricks Y coordinate
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140#setting the third row of bricks Y coordinate
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
# Add the paddle and the ball to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# Main Loop
while carryOn:
    #Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
    #Moving the paddle when the use uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
 
    #Game logic should go here
    all_sprites_list.update()
 
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:#cheking if the ball touched the bottom of the screen
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
    if ball.rect.y<40:#looking if the ball bounced on the top of the screen
        ball.velocity[1] = -ball.velocity[1]
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
 
    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()