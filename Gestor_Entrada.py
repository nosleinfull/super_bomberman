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
Classe responsavel por gerenciar todas as entradas, a principio so foi usado as entradas do teclado
pode-se ainda porgramar aqui entras de servidor, joypad e etc
"""
import pygame
import sys


class GestorEntrada():


	def __init__(self):
		pass

	def getListaComandos(self,listaComandosAtivos):
				

		Keys = pygame.key.get_pressed()

	   	for i in range (len( Keys)):

	   		if Keys[i] == 1:

	   			listaComandosAtivos.append(i)  
	   			
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		    	sys.exit()		
		
	def ajustaListaComandos(self, listaComandosAtivos, listaPersonagem):

		listaFinal = []
		LF = []
		flag  = 1
		flag2 = 1
		for i in range (len (listaComandosAtivos)):

			for j in range (len(listaPersonagem)):

				if (i > 1):
					break

				if (j < 4 and listaComandosAtivos[i] == listaPersonagem[j] and flag):
					listaFinal.append(listaComandosAtivos[i])
					flag = 0

				if (j >= 4 and listaComandosAtivos[i] == listaPersonagem[j] and flag2):		
					listaFinal.append(listaComandosAtivos[i])
					flag2 = 0

		
		return listaFinal			

	def getListaFinal(self):
		return self.listaFinal