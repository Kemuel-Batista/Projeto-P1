import pygame
from tkinter import messagebox
from cesta import Cesta
from frutas import Fruta

pygame.init()
janela = pygame.display.set_mode((695,495))
fundo = pygame.image.load('fundo1.png')
fundo2 = pygame.image.load('fundo2.png')
pygame.display.set_caption("Feira Maluca")

cesta = Cesta(janela)
melancia = Fruta(janela, 'melancia.png', 60, 32)
banana = Fruta(janela, 'banana.png', 60, 45)
uva = Fruta(janela, 'uva.png', 60, 40)
morango = Fruta(janela, 'morango.png', 50, 32)
laranja = Fruta(janela, 'laranja.png', 60, 60)

font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 20)

time = 30
play = False
janela_aberta = True
while janela_aberta:
    if play == False:
        text = font.render('JOGAR', True, (0, 50, 250), None)
        janela.blit(fundo, (0, 0))
        janela.blit(text, (285, 250))
        if 285 <= pygame.mouse.get_pos()[0] <= 400 and 250 <= pygame.mouse.get_pos()[1] <= 280:
            text = font.render('JOGAR', True, (0, 130, 250), None)
            janela.blit(text, (285, 250))
            if pygame.mouse.get_pressed()[0]:
                play = True

    if play == True:
        time -= 0.05      
        if time <= 0:
            messagebox.showinfo("Oops seu tempo acabou!", (f"Você conseguiu pegar:\n{banana.score} bananas;\n{uva.score} uvas;\n{morango.score} morangos;\n{laranja.score} laranjas;\n{melancia.score} melancias."))
            if not messagebox.askyesno("Oops seu tempo acabou!", "Deseja jogar novamente?"):
                janela_aberta = False
            else:
                time = 30
                Fruta.reseta_score(melancia, uva, banana, laranja, morango)
                
        janela.blit(fundo2, (0, 0))
        Fruta.frutas_cesta_jogo(melancia, banana, uva, morango, laranja, cesta) 

        timer = font.render(str(int(time)), True, (0, 0, 0), None)
        janela.blit(timer, (40, 465))
        
        score_banana = font_score.render(str(banana.score), True, (0, 0, 0), None)
        score_uva = font_score.render(str(uva.score), True, (0, 0, 0), None)
        score_morango = font_score.render(str(morango.score), True, (0, 0, 0), None)
        score_laranja = font_score.render(str(laranja.score), True, (0, 0, 0), None)
        score_melancia = font_score.render(str(melancia.score), True, (0, 0, 0), None)

        Fruta.insere_score(score_banana, score_uva, score_morango, score_laranja, score_melancia, janela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    pygame.display.update()

pygame.quit()