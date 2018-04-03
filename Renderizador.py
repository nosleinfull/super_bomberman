"""
Universidade Estadual de Mato Grosso do Sul
Topicos em Computacao I  Trabalho I

Autor:
Leandro Souza da Silva
Nielson Fernandes Silva

Data 2014
"""

#! usr/bin/python

"""
Objetivo: Renderizar os objetos passdos por uma lista
"""

import pygame


class ProcessadorGrafico():


	def __init__(self, largura, altura, timeClock):

		self.largura = largura
		self.altura  = altura
		self.clock   = pygame.time.Clock()
		self.timeClock = timeClock
		self.screen = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
		self.screen.fill((255, 255, 255))

	def getLarguraTela(self):
		return self.largura

	def getAlturaTela(self):
		return self.altura

	def getClock(self):
		return self.clock	


	def render(self, matrizObjetos):


		for i in range (len(matrizObjetos)):

			for j in range (len (matrizObjetos[0])):

				lis = matrizObjetos[i][j]

				for k in lis:

					if (k != None and k.getNome() != 'personagem'):
						
						image = k.getConjuntoImg()
						x = k.getIndexConjuntoImgX()
						y = k.getIndexConjuntoImgY()


						self.screen.blit(image[x][y], (k.posicao[0], k.posicao[1]))
		
		#aqui ferrou tudo 
		for i in range (len(matrizObjetos)):

			for j in range (len (matrizObjetos[0])):

				lis = matrizObjetos[i][j]

				for k in lis:

					if (k != None and k.getNome() == 'personagem'):
						
						image = k.getConjuntoImg()
						x = k.getIndexConjuntoImgX()
						y = k.getIndexConjuntoImgY()
						self.screen.blit(image[x][y],  (k.posicao[0], k.posicao[1]-20))
						

		pygame.display.flip()
		self.clock.tick(self.timeClock)


	def render2(self, image, px, py):
		self.screen.blit(image,  (px, py))
		
	def updateScreen(self):
		self.clock.tick(self.timeClock)
		pygame.display.flip()
		

	