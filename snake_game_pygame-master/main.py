#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random, time
from pygame.locals import *

# Pygame
pygame.init()
mainClock = pygame.time.Clock()

# Window
WINDOWWIDTH = 450
WINDOWHEIGHT = 450
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('SNAKE do PAULO')

# variaveis de movimento
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

# Cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake
engorda = 1
snakeTAMANHO = 15
snake = pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT/2, snakeTAMANHO, snakeTAMANHO)
# Trajecto - a lista depois vai avancando, o que estava a tras avanca para o sitio onde tava o snake k ia a frente, criando efeito de animacao -> snakeROTA[0] - cabeca da snake
snakeROTA = []
snakeROTA.append(snake)

# Comida
nFood = 0
foodTAMANHO = 15
food = []

# lista de posicoes de aparecimento de food, multiplos do tamanho da snake, para a snake e a food ficarem alinhados. e food nao aparecer em cima da snake
foodCOORDENADAS = []
for i in range(WINDOWWIDTH-snakeTAMANHO):
    if i%snakeTAMANHO==0 and i not in snakeROTA:
		foodCOORDENADAS.append(i)

MOVESPEED = snakeTAMANHO

# confirmar se e gameover - ver se cobra bate nela mesma
gameover=0
confirmacaoFOOD=0
def GAMEOVER():
	r=range(len(snakeROTA))
	if confirmacaoFOOD==0:
		for key in r:
			if key!=0 and snakeROTA[key]==snakeROTA[0]:
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.5)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.2)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.2)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(5)
				gameover=1
				return gameover	
	if confirmacaoFOOD==1:
		for key in r:
			if key!=0 and key!=r[-1] and snakeROTA[key]==snakeROTA[0]:
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.5)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.2)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(0.2)
				windowSurface.fill(BLACK)
				pygame.display.update()
				time.sleep(0.2)
				for i in snakeROTA:
					pygame.draw.rect(windowSurface, RED, i)
				pygame.display.update()
				time.sleep(5)
				gameover=1
				return gameover



# game loop start
while True:
	# check for events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			# change the keyboard variables
			if (event.key == K_LEFT or event.key == ord('a')) and moveRight != True:
				moveLeft = True
				moveRight = False
				moveUp = False
				moveDown = False
			elif (event.key == K_RIGHT or event.key == ord('d')) and moveLeft != True:
				moveRight = True
				moveLeft = False
				moveUp = False
				moveDown = False
			elif (event.key == K_UP or event.key == ord('w')) and moveDown != True:
				moveUp = True
				moveDown = False
				moveLeft = False
				moveRight = False
			elif (event.key == K_DOWN or event.key == ord('s')) and moveUp != True:
				moveDown = True
				moveUp = False
				moveLeft = False
				moveRight = False
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	#redefine o valor, serve para o gameover distinguir a food de uma colisao
	confirmacaoFOOD=0
				
	# draw the black background onto the surface
	windowSurface.fill(BLACK)



	# mover snake e acrescenta nova entrada na lista snakeROTA
	if moveDown:
		copia = pygame.Rect.copy(snakeROTA[0])
		copia.bottom += MOVESPEED
		snakeROTA.insert(0, copia)
	if moveUp:
		copia = pygame.Rect.copy(snakeROTA[0])
		copia.top -= MOVESPEED
		snakeROTA.insert(0, copia)
	if moveLeft:
		copia = pygame.Rect.copy(snakeROTA[0])
		copia.left -= MOVESPEED
		snakeROTA.insert(0, copia)
	if moveRight:
		copia = pygame.Rect.copy(snakeROTA[0])
		copia.right += MOVESPEED
		snakeROTA.insert(0, copia)

	# actualizar lista snakeROTA, adicionando snake em index 0 e removendo indexs no final que sao maiores k o tamanho da snake
	if len(snakeROTA) != engorda:
		snakeROTA.pop()



	# draw snake e sub SNAKES
	for i in snakeROTA:
		pygame.draw.rect(windowSurface, WHITE, i)
		


	# draw food
	food.append(pygame.Rect(random.choice(foodCOORDENADAS), random.choice(foodCOORDENADAS), foodTAMANHO, foodTAMANHO))
	pygame.draw.rect(windowSurface, GREEN, food[0])

	# quando snake come food
	if snakeROTA[0].colliderect(food[0]) == True:
		food.remove(food[0])
		engorda += 1
		confirmacaoFOOD=1 #serve para o gameover distinguir e nao accionar
		snakeROTA.append(snakeROTA[0])
	
	# verificar gameover
	GAMEOVER()
	if gameover==1:
		break
	
	# draw the window onto the screen
	pygame.display.update()
	mainClock.tick(10)

