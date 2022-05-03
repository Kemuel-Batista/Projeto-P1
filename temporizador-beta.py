import pygame

class Temporizador:
    pygame.init()
    janela = pygame.display.set_mode((100, 100))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    tempo = 15
    text = font.render(str(tempo), True, (0, 12, 0))

    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                tempo -= 1
                text = font.render(str(tempo), True, (0, 12, 0))
                if tempo == 0:
                    pygame.time.set_timer(timer_event, 0)                

        janela.fill((255, 255, 255))
        text_rect = text.get_rect(center = janela.get_rect().center)
        janela.blit(text, text_rect)
        pygame.display.flip()