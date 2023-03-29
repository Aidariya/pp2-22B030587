import pygame
pygame.init()

prev_b = pygame.image.load("images/previous.png")
play_b = pygame.image.load("images/play.png")
next_b = pygame.image.load("images/next.png")

num_mus = 0

music_list = [pygame.mixer.Sound("shakira.mp3"),
            pygame.mixer.Sound("menseni.mp3"),
            pygame.mixer.Sound("fakelove.mp3")
            ]

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Music player")

running = True
while running:
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,255,255), (0, 400, 500, 200))
    screen.blit(prev_b, (125, 480))
    screen.blit(play_b, (230, 480))
    screen.blit(next_b, (325, 480))
    pygame.display.update()

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            music_list[num_mus].play()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RCTRL:
            music_list[num_mus].stop()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            music_list[num_mus].stop()
            num_mus += 1
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            music_list[num_mus].stop()
            num_mus -= 1
        

    if num_mus > len(music_list)-1:
        num_mus = 0
    elif num_mus < 0:
        num_mus = 2