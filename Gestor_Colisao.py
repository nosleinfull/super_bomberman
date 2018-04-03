"""
Universidade Estadual de Mato Grosso do Sul
Topicos em Computacao I  Trabalho I

Autor:
Leandro Souza da Silva
Nielson Fernandes Silva

Data 2014
"""

#! usr/bin/python

class GestorColisao():



	def __init__(self):
		pass


	def calculaMudancaLista(self, constante, objCoord, chaoCoord, limite):

		if (abs((constante + objCoord) - chaoCoord ) >= limite):
			#print abs(constante + objCoord - chaoCoord )
			return True

		else:
			False	


	def dif(p1,p2):
	
		x = p1[0] - p2[0]
		y = p1[1] - p2[1]
		
		list =[x,y]
		
		return list
		
			
	def calculaMeio(self, personagem, chao, constante):
	
		
		if (personagem.posicao[0] == chao.posicao[0] and ( (personagem.posicao[1] + constante) == chao.posicao[1]))	:
			return True

		else:
			
			False	

		