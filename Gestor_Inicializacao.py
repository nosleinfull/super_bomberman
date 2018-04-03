"""
Universidade Estadual de Mato Grosso do Sul
Topicos em Computacao I  Trabalho I

Autor:
Leandro Souza da Silva
Nielson Fernandes Silva

Data 2014
"""

#! usr/bin/python

from Objetos import *
from Renderizador import *
from Gestor_Entrada import *
from Gestor_Regras import *

import pygame.locals
import ConfigParser
import string
import pickle
import pygame
import time
import random
import pygame



"""
processador inicial de jogo, carrega uma matriz com todos os objetos do jogo
e um dicionario contendo tudo, o mapa, e os demais objetos com suas respecetivas
folhas de sprites cortada
Obs: os indices do dicionario sao baseados no arquivo de configuracao
"""

class ProcessadorInicialDeJogo():

	def __init__(self, nome_arquivo):

		self.matrizObjetos = []
		self.dic = {}
		self.cenario = []
		self.parser = ConfigParser.ConfigParser()
		self.parser.read(nome_arquivo)

		#carrega o dicionario
		self.__carregaDicionario()

		#atuliza dicionario com as imagens de cada opcao
		self.__carregaTileDic()
		#print self.dic
			#carrega o cenario
		self.__carregaCenario()

		self.__carregaListaObjetos()

		self.__setMatizPosicoes()

		self.__setPlayerPosicao()



	#metodo para carregar informacoes de um arquivo para um dicionario
	#as informacoes podem ser vistas e alteradas no arquivo de configuracao
	def __carregaDicionario(self):

		for i in self.parser.sections():

			try:
				lis = []
				lis.append(self.parser.get(i, 'nome'))
				lis.append(self.parser.get(i, 'sprite'))
				lis.append(self.parser.get(i, 'largura'))
				lis.append(self.parser.get(i, 'altura'))					
				lis.append(self.parser.get(i, 'lista_comandos').split())
				lis.append(self.parser.get(i, 'limite_mudanca_estados'))
				lis.append(self.parser.get(i, 'tempo_duracao_frames'))


				self.dic[i] = lis

			except ConfigParser.NoOptionError, a:
				if (i == 'mapa'):
					lis.append(self.parser.get(i, 'cenario').split())
					self.dic[i] = lis
				

		for i in self.dic:
			
			if (i >= 'P' and i <= 'Z'):
				lis = []
				for j in range (len (self.dic[i][4])):
					lis.append(int(self.dic[i][4][j]))
				self.dic[i][4] = lis
		

		#print self.dic
	#carrega os tiles especificos de cada opcao do arquivo
	def __carregaTileDic(self):
		for i in self.dic:
			
			if (i != 'mapa'):
				
				self.dic[i].append(self.__carregaTile(self.dic[i][1],int (self.dic[i][2]),int (self.dic[i][3])))		
			

	#metodo para carregar informacoes do dicionario para uma lista simples
	def __carregaCenario(self):
		self.cenario = self.dic['mapa'][0]
		pass


	#funcao para fazer um corte numa dada image e retorna uma matriz de imagens
	def __carregaTile(self, nomeArquivo, largura, altura):

		try:

			image = pygame.image.load(nomeArquivo)
		
		except pygame.error, E:

			print "Erro, arquivo na econtrado!", nomeArquivo
			return []


		image_largura, image_altura = image.get_size()
		limiteLargura = image_largura/largura
		limiteAltura  = image_altura/altura
		listaTiles = []


		#corta as imagens e as poem em uma lista
		for i in range (limiteAltura):

			linha = []
			listaTiles.append(linha)

			for j in range (limiteLargura):

				rect = (j * largura, i * altura, largura, altura)
				linha.append(image.subsurface(rect))	

		return listaTiles
	
	#funcao para constuir matriz de objetos para o inicio do jogo
	def __carregaListaObjetos(self):
		

		for i in range (len(self.cenario)):

			listaObjetos = []

			for j in range (len(self.cenario[0])):
						# Pa   c     e     b     t       P
				lista = [None, None, None, None, None, None]

				char = self.cenario[i][j]


				#Aqui devera ser acresentada condicoes para os demais objetos
				if (char == '#' ):
					
					lista[0] = Objeto(self.dic[char][7], self.dic[char][0], [i,j], int(self.dic[char][2]), int (self.dic[char][3]))

				elif (char == '.'):
					
					lista[1] = Objeto(self.dic[char][7], self.dic[char][0], [i,j], int(self.dic[char][2]), int (self.dic[char][3]))


				elif (char == '*'):

					lista[4] = Tijolos(self.dic[char][7], self.dic[char][0], [i,j], int(self.dic[char][5]),  int(self.dic[char][6]), int (self.dic[char][2]), int(self.dic[char][3]))
					lista[1] = Objeto(self.dic['.'][7], self.dic['.'][0], [i,j], int (self.dic['.'][2]), int (self.dic['.'][3])) 

				elif (char >= 'P' and char <= 'Z'):

					lista[5] = Personagem(self.dic[char][7], self.dic[char][0], [i,j], int (self.dic[char][5]),int (self.dic[char][6]), int (self.dic[char][2]),int (self.dic[char][3]),self.dic[char][4])
					lista[1] = Objeto(self.dic['.'][7], self.dic['.'][0], [i,j], int (self.dic['.'][2]), int (self.dic['.'][3]))

				listaObjetos.append(lista)

			self.matrizObjetos.append(listaObjetos)
	
	def __setMatizPosicoes(self):


		for i in range (len(self.matrizObjetos)):

				for j in range (len (self.matrizObjetos[0])):

					lis = self.matrizObjetos[i][j]

					for k in lis:

						if (k != None and k.getNome() != 'personagem'):
							
							image = k.getConjuntoImg()
							x = k.getIndexConjuntoImgX()
							y = k.getIndexConjuntoImgY()

							k.posicao[0] =  j*k.getLarguraImg()
							k.posicao[1] =  i*k.getAlturaImg()
						

	def __setPlayerPosicao(self):
	
		for i in range (len(self.matrizObjetos)):

			for j in range (len (self.matrizObjetos[0])):

				lis = self.matrizObjetos[i][j]

				for k in lis:

					if(k != None and k.getNome() == 'personagem'):

						k.posicao[0] = lis[1].getAlturaImg() * j
						k.posicao[1] = (lis[1].getLarguraImg() *i)-20
						

	#metodo para retornar o dicionario		
	def getDic(self):
		return self.dic

	#metodo para retornar a matriz de objetos
	def getMatrizObjetos(self):
		return self.matrizObjetos	
