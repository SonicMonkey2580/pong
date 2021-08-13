import pygame
from pygame import font
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddle_A = Paddle(RED, 10 ,100)
paddle_A.rect.x = 20
paddle_A.rect.y = 200

paddle_B = Paddle(BLUE, 10 ,100)
paddle_B.rect.x = 670
paddle_B.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle_A)
all_sprites_list.add(paddle_B)
all_sprites_list.add(ball)

carry_on = True 

clock  = pygame.time.Clock()

scoreA = 0
scoreB = 0

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carry_on = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_A.move_up(5)
    if keys[pygame.K_s]:
        paddle_A.move_down(5)
    if keys[pygame.K_UP]:
        paddle_B.move_up(5)
    if keys[pygame.K_DOWN]:
        paddle_B.move_down(5)

    #Game logic should go here
    all_sprites_list.update()


    if ball.rect.x>=690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle_A) or pygame.sprite.collide_mask(ball, paddle_B):
        ball.bounce()

   

    #drawing code should go here
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)

    if scoreA > 0:
        text = font.render(str(scoreA), 1, RED)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text,(420,10))
    elif scoreB > 0:
        text = font.render(str(scoreA), 1, RED)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text,(420,10))
    else:
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text,(420,10))

    pygame.display.flip()


    clock.tick(60)

pygame.quit()