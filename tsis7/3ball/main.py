import pygame
pygame.init()

clock = pygame.time.Clock()

w = 500
h = 700 
screen = pygame.display.set_mode((w,h))
ball_x = w/2
ball_y = h/2
running = True
while running:
    clock.tick(30)

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0 , 0),(ball_x, ball_y), 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and ball_x < w-50:
        ball_x += 20
    elif keys[pygame.K_LEFT] and ball_x > 50:
        ball_x -= 20
    elif keys[pygame.K_DOWN] and ball_y < h -50:
        ball_y += 20
    elif keys[pygame.K_UP] and ball_y > 50:
        ball_y -= 20