import pygame
from tkinter import messagebox
from cesta import Cesta
from frutas import Fruta
from random import randint

pygame.init()
janela = pygame.display.set_mode((695,495))  #define o tamanho da janela

#carrega as duas imagens usadas para o fundo
fundo = pygame.image.load('fundo1.png')
fundo2 = pygame.image.load('fundo2.png')

#título da aba
pygame.display.set_caption("Feira Cin")

#cria as instâncias
cesta = Cesta(janela)
cronometro = Fruta(janela, 'cronometro.png', 40, 40)
melancia = Fruta(janela, 'melancia.png', 60, 32)
banana = Fruta(janela, 'banana.png', 60, 45)
uva = Fruta(janela, 'uva.png', 60, 40)
morango = Fruta(janela, 'morango.png', 50, 32)
laranja = Fruta(janela, 'laranja.png', 60, 60)

#carrega o tipo e tamanho das fontes do texto, score e temporizador
font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 20)

time = 30  #valor inicial do temporizador
play = False  #enquanto não estiver jogando
janela_aberta = True  #enquanto a janela estiver aberta

#loop da tela do jogo
while janela_aberta:

    #se play for False exibir fundo 1 e botão jogar
    if play == False:
        text = font.render('JOGAR', True, (0, 50, 250), None)
        janela.blit(fundo, (0, 0))
        janela.blit(text, (285, 250))  #"jogar"

        #se o mouse estiver em cima do botão jogar, muda a cor do texto
        if 285 <= pygame.mouse.get_pos()[0] <= 400 and 250 <= pygame.mouse.get_pos()[1] <= 280:
            text = font.render('JOGAR', True, (0, 130, 250), None)
            janela.blit(text, (285, 250))

            #se mouse clicar no botão, play recebe True e jogo começa
            if pygame.mouse.get_pressed()[0]:
                play = True

    #se play for True, jogo começa e temporizador começa a contar 
    if play == True:
        time -= 0.05

        #quando o tempo acabar, abre uma messagebox com os valores da coleta     
        if time <= 0:
            messagebox.showinfo("Oops seu tempo acabou!", (f"Você conseguiu pegar:\n{banana.score} bananas;\n{uva.score} uvas;\n{morango.score} morangos;\n{laranja.score} laranjas;\n{melancia.score} melancias.\nTotal: {banana.score+uva.score+morango.score+laranja.score+melancia.score}"))

            #abre messagebox perguntando se quer jogar novamente
            if not messagebox.askyesno("Oops seu tempo acabou!", "Deseja jogar novamente?"):
                janela_aberta = False #caso não, janela fecha
            
            #caso sim, temporizador e score resetam
            else:
                time = 30
                Fruta.reseta_score(melancia, uva, banana, laranja, morango)
                
        janela.blit(fundo2, (0, 0))  #exibe fundo2

        #insere as frutas e a cesta na tela com os movimentos e as colisões
        Fruta.frutas_cesta_jogo(melancia, banana, uva, morango, laranja, cronometro, cesta)

        timer = font.render(str(int(time)), True, (0, 0, 0), None) #transforma o valor em decimal do temporizador
        janela.blit(timer, (40, 465))  #exibe o valor transformado do timer na tela
        
        #transforma o valor dos scores de cada fruta
        score_banana = font_score.render(str(banana.score), True, (0, 0, 0), None)
        score_uva = font_score.render(str(uva.score), True, (0, 0, 0), None)
        score_morango = font_score.render(str(morango.score), True, (0, 0, 0), None)
        score_laranja = font_score.render(str(laranja.score), True, (0, 0, 0), None)
        score_melancia = font_score.render(str(melancia.score), True, (0, 0, 0), None)
        
        #exibe scores na tela
        Fruta.insere_score(score_banana, score_uva, score_morango, score_laranja, score_melancia, janela)
        
        #caso jogador colete um temporizador, um tempo bonus aleatório é adicionado e objeto é realocado em uma nova distância aleatória 
        if cronometro.score == 1:
            cronometro.score = 0
            time += randint(5, 15)
            cronometro.y = -(randint(3300, 5200))

    #se usuário clicar em fechar a aba janela fecha e programa encerra
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    pygame.display.update()  #atualiza a tela

pygame.quit()