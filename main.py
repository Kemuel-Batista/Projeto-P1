import pygame
from tkinter import messagebox
from cesta import Cesta
from frutas import Fruta

pygame.init()
janela = pygame.display.set_mode((700,500))
fundo = pygame.image.load('fundo1.png')
pygame.display.set_caption("Feira Maluca")

cesta = Cesta(janela)
melancia = Fruta(janela, 'melancia.png', 60, 32)
banana = Fruta(janela, 'banana.png', 60, 45)
uva = Fruta(janela, 'uva.png', 60, 40)
morango = Fruta(janela, 'morango.png', 50, 32)
laranja = Fruta(janela, 'laranja.png', 60, 60)

font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 20)

madeira = pygame.transform.scale(pygame.image.load('madeira.png'), (700, 40))
temporizador = pygame.transform.scale(pygame.image.load('cronometro.png'), (30, 30))
banana_score = pygame.transform.scale(pygame.image.load('banana.png'), (30, 30))
uva_score = pygame.transform.scale(pygame.image.load('uva.png'), (35, 30))
morango_score = pygame.transform.scale(pygame.image.load('morango.png'), (30, 30))
laranja_score = pygame.transform.scale(pygame.image.load('laranja.png'), (40, 40))
melancia_score = pygame.transform.scale(pygame.image.load('melancia.png'), (25, 19))

time = 10
janela_aberta = True
while janela_aberta:
    time -= 0.05
    if time <= 0:
        messagebox.showinfo("Oops seu tempo acabou!", (f"Você conseguiu pegar:\n{banana.score} bananas;\n{uva.score} uvas;\n{morango.score} morangos;\n{laranja.score} laranjas;\n{melancia.score} melancias."))
        if not messagebox.askyesno("Oops seu tempo acabou!", "Deseja jogar novamente?"):
            janela_aberta = False
        else:
            time = 30
            Fruta.reseta_score(melancia, uva, banana, laranja, morango)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    janela.blit(fundo, (0, 0)) #inserir fundo 
    Fruta.frutas_cesta_jogo(melancia, banana, uva, morango, laranja, cesta) 

    janela.blit(madeira, (0, 460))
    timer = font.render(str(int(time)), True, (0, 0, 0), None)
    janela.blit(timer, (40, 465))

    score_banana = font_score.render(str(banana.score), True, (0, 0, 0), None)
    score_uva = font_score.render(str(uva.score), True, (0, 0, 0), None)
    score_morango = font_score.render(str(morango.score), True, (0, 0, 0), None)
    score_laranja = font_score.render(str(laranja.score), True, (0, 0, 0), None)
    score_melancia = font_score.render(str(melancia.score), True, (0, 0, 0), None)

    janela.blit(score_banana, (300, 470))
    janela.blit(score_uva, (380, 470))
    janela.blit(score_morango, (460, 470))
    janela.blit(score_laranja, (540, 470))
    janela.blit(score_melancia, (620, 470))

    janela.blit(temporizador, (5, 465))
    janela.blit(banana_score, (260, 465))
    janela.blit(uva_score, (340, 465))
    janela.blit(morango_score, (420, 465))
    janela.blit(laranja_score, (500, 460))
    janela.blit(melancia_score, (580, 470))

    pygame.display.update()

pygame.quit()