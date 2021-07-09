import pygame
from paddle import Paddle
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddle_A = Paddle(WHITE, 10 ,100)
paddle_A.rect.x = 20
paddle_A.rect.y = 200

paddle_B = Paddle(WHITE, 10 ,100)
paddle_B.rect.x = 670
paddle_B.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle_A)
all_sprites_list.add(paddle_B)

carry_on = True 

clock  = pygame.time.Clock()

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carry_on = False 

    #Game logic should go here
    all_sprites_list.update()

    #drawing code should go here
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()