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
Objetivo: aplicar regras a cada obejto que compoe o jogo,
cada objeto e submetido a conjunto de regras a fim de que
o jogo seja parecido com o original
"""

from Gestor_Colisao import *
from Objetos import *

class GestorRegras():


	def __init__(self):
		
		self.gestorColisao = GestorColisao()
		self.duracao = 0
		self.morre = True

		
	#implementar aqui tudo o que o persoangem faz no jogo baseado nas regras do gestor
	def geriPersonagem(self, i, j, k, personagem, matrizObjetos, listaComandos, dicionarioObjetos):

		#estado vivo

		if (personagem.estado == 0):

			matrizObjetos[i][j][k] = None
		
		else:

			if (matrizObjetos[i][j][2] != None):
				personagem.listaMetodosAnimacao[1] = True
				personagem.listaMetodosAcao[0] = True
				

			if (personagem.listaMetodosAnimacao[1] == True):
				personagem.AnimaAcao(4)

			if (personagem.listaMetodosAcao[0] == True):
				personagem.Acao(4)
						
					
			if (personagem.listaMetodosAnimacao[1] != True and personagem.listaMetodosAcao[0] != True):
				
				for q in range (len(listaComandos)):
					#print "Infinito: ", listaComandos 
					#movimento para cima
					if (listaComandos[q] == personagem.ListaComandos[0]):

						lisCima    =  matrizObjetos[i-1][j]
						
						if ( (lisCima[0] != None or lisCima[3] != None or lisCima[4] != None) and self.gestorColisao.calculaMeio(personagem, matrizObjetos[i][j][1], 20)):
							
							personagem.AnimaAcao(0)
						
						else:	
								
							if ((abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) >= 0) and  (abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) <  12)):
								
								if ((abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) == 0)):
									
									personagem.AnimaAcao(0)	
									personagem.Acao(0)
									self.geriMudancaLista(matrizObjetos,20, personagem, 1, i, j, k, -1, 0)

								else:
									
									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j, k, personagem.indexConjuntoImgX)						
										

							elif (abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) >= 12):


								personagem.AnimaAcao(personagem.indexConjuntoImgX)
								personagem.Acao(personagem.indexConjuntoImgX)
								self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j,k, personagem.indexConjuntoImgX)
								

					#movimento para baixo
					elif (listaComandos[q] == personagem.ListaComandos[1]):
						
						lisBaixo = matrizObjetos[i+1][j]
						
						#verifica a lista acima se houver parede, tijolo, e bomba, so anima e nao se move
						if ((lisBaixo[0] != None or lisBaixo[3] != None or lisBaixo[4] != None) and self.gestorColisao.calculaMeio(personagem, matrizObjetos[i][j][1], 20)):
							personagem.AnimaAcao(1)
							
						else:

							if ((abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) >= 0) and  (abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) <  12)):
								
								if ((abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) == 0)):

									personagem.AnimaAcao(1)	
									personagem.Acao(1)
									self.geriMudancaLista(matrizObjetos,20, personagem, 1, i, j, k,1, 0)

								else:
									
									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j, k, personagem.indexConjuntoImgX)						
										

							elif (abs(personagem.posicao[0] - matrizObjetos[i][j][1].posicao[0]) >= 12):
									
									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j,k, personagem.indexConjuntoImgX)
								
					#move para direita		
					elif (listaComandos[q] == personagem.ListaComandos[2]):
						
						lisDireita = matrizObjetos[i][j+1]
						
						#verifica a lista acima se houver parede, tijolo, e bomba, so anima e nao se move
						if ((lisDireita[0] != None or lisDireita[3] != None or lisDireita[4] != None)   and self.gestorColisao.calculaMeio(personagem, matrizObjetos[i][j][1], 20)):
							personagem.AnimaAcao(2)

						else:

							if ( (abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) >= 0)  and (abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) < 12)) :
							
								if ((abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) == 0)):
									
							
									personagem.Acao(2)
									personagem.AnimaAcao(2)
									self.geriMudancaLista(matrizObjetos, 0, personagem, 0, i, j, k, 0, 1)
							
								else:

									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j, k,personagem.indexConjuntoImgX)

							elif ((abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) >= 12)):
									
									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j,k, personagem.indexConjuntoImgX)		


					#move para esquerda
					elif (listaComandos[q] == personagem.ListaComandos[3]):
											
						lisEsquerda = matrizObjetos[i][j-1]
						
						#verifica a lista acima se houver parede, tijolo, e bomba, so anima e nao se move
						if ((lisEsquerda[0] != None or lisEsquerda[3] != None or lisEsquerda[4] != None)  and self.gestorColisao.calculaMeio(personagem, matrizObjetos[i][j][1], 20)):
							personagem.AnimaAcao(3)

						else:

							if ( (abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) >= 0)  and (abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) < 12)) :
							
								if ((abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) == 0)):

									personagem.Acao(3)
									personagem.AnimaAcao(3)
									self.geriMudancaLista(matrizObjetos, 0, personagem, 0, i, j, k, 0, -1)
							
								else:

									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j, k, personagem.indexConjuntoImgX)

							elif ((abs(personagem.posicao[1] + 20 - matrizObjetos[i][j][1].posicao[1]) >= 12)):

									personagem.AnimaAcao(personagem.indexConjuntoImgX)
									personagem.Acao(personagem.indexConjuntoImgX)
									self.atualizaMudancaMatriz(matrizObjetos,personagem,  i, j, k, personagem.indexConjuntoImgX)

							


					elif (listaComandos[q] == personagem.ListaComandos[4]):
						self.criaBomba(i, j, matrizObjetos, dicionarioObjetos, personagem.ListaPoder[1]+8)
						
					elif (listaComandos[q] == personagem.ListaComandos[5]):
						pass
					elif (listaComandos[q] == personagem.ListaComandos[6]):
						pass
				
				if (len(listaComandos) == 0):
					
						personagem.AnimaParado()

					


		#comportamento comum de varias condicoes, norte, sul, leste, oeste	
	def geriMudancaLista(self, matrizObjetos,cons, personagem, pos, i, j, k, Ie, Je):

			chaoCord    =  matrizObjetos[i][j][1].posicao[pos]
			limiteChao  =  matrizObjetos[i][j][1].getLarguraImg() 
			trocarLista =  self.gestorColisao.calculaMudancaLista(cons, personagem.posicao[pos],chaoCord,limiteChao)
			
			if (trocarLista == True):

				if (matrizObjetos[i+Ie][j+Je][5] == None):
					
					matrizObjetos[i+Ie][j+Je][5] = matrizObjetos[i][j][k]
					
					if (k == 5):
						matrizObjetos[i][j][k] = None
					else:	
					
						del matrizObjetos[i][j][k] 
				else:
				
					matrizObjetos[i+Ie][j+Je].append(matrizObjetos[i][j][k])	
					matrizObjetos[i][j][k] = None	
				
				
	def atualizaMudancaMatriz(self, matrizObjetos, personagem, i, j, k, index):

		if(index == 0):
			self.geriMudancaLista(matrizObjetos,20, personagem, 1, i, j, k, -1, 0)

		elif(index == 1):
			self.geriMudancaLista(matrizObjetos, 20, personagem, 1, i, j, k, 1, 0)


		elif(index == 2):
			self.geriMudancaLista(matrizObjetos, 0, personagem, 0, i, j, k, 0, 1)

		elif(index == 3):
			self.geriMudancaLista(matrizObjetos, 0, personagem, 0, i, j, k, 0, -1)


	#implementar aqui tudo o que a bomba pode fazer no jogo baseado nas regras do gestor	
	def geriBomba(self, i, j, bomba, matrizObjetos, dic):	
		
		# Se a bomba esta Viva ( Fora de explosao e ainda nao explodio )
		if(matrizObjetos[i][j][3].getEstado() == 1 and matrizObjetos[i][j][2] == None):
		
			matrizObjetos[i][j][3].AnimaAcao(0)
			matrizObjetos[i][j][3].Acao(4)
		
		# A bomba esta morta
		else:
		
			Raio = matrizObjetos[i][j][3].RaioAlcance
			
			# Destroi a Bomba
			matrizObjetos[i][j][3] = None
			
			# Cria Explosao
			self.criaExplosao(i,j,matrizObjetos,dic,Raio)
			
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			# Movimentos e Colisao Aqui
			pass

	# Cria uma nova Instancia de uma bomba
	def criaBomba(self,i,j,matrizObjetos, dic,RaioAlcance):
		
		
		if(matrizObjetos[i][j][0] == None and matrizObjetos[i][j][3] == None and matrizObjetos[i][j][4] == None):
			pos = matrizObjetos[i][j][1].getPosicao()
			matrizObjetos[i][j][3] = Bomba(dic['B'][7], dic['B'][0], pos, int (dic['B'][5]),int (dic['B'][6]), int (dic['B'][2]),int (dic['B'][3]),RaioAlcance)
	
	#implementar aqui tudo o que o tijolo pode fazer no jogo baseado nas regras do gestor
	def geriTijolo(self, i, j, tijolo, matrizObjetos, dic):
		
		if( matrizObjetos[i][j][4].getEstado() == 0):

			matrizObjetos[i][j][4] = None
			
		else:
			
			if( matrizObjetos[i][j][2] != None ):
				
				# Animacao 0 em Estado Ativado
				matrizObjetos[i][j][4].listaMetodosAnimacao[0] = True
				
				# Acao 0 em Estado Ativado
				matrizObjetos[i][j][4].listaMetodosAcao[0] = True

			if(matrizObjetos[i][j][4].listaMetodosAnimacao[0] == True):
				
				matrizObjetos[i][j][4].animaAcao(1)
				
			if(matrizObjetos[i][j][4].listaMetodosAcao[0] == True):
				
				matrizObjetos[i][j][4].acao(1)
		
	#implementar aqui tudo o que a explosao pode fazer no jogo baseado nas regras do gestor
	def geriExplosao(self, i, j, explosao, matrizObjetos, dic):
		
		if(explosao.getEstado() != 0):
		
			matrizObjetos[i][j][2].AnimaAcao(0)
			matrizObjetos[i][j][2].Acao(0)
			
		else:
		
			matrizObjetos[i][j][2] = None
			
	# Cria uma Explosao
	def criaExplosao(self, i,j, matrizObjetos, dic, Raio):
		
		pos = matrizObjetos[i][j][1].getPosicao()
		# Se nao existir uma explosao, cria uma explosao
		if(matrizObjetos[i][j][2] == None):
		
			matrizObjetos[i][j][2] = Explosao(dic['E'][7], dic['E'][0], pos, int (dic['E'][5]),int (dic['E'][6]), int (dic['E'][2]),int (dic['E'][3]))
			matrizObjetos[i][j][2].SetTipoExplosao(4)
		
		
		# Norte 
		self.ExplosaoDir(i,j,-1,0,0,5,matrizObjetos,dic, Raio)
		
		# Sul 
		self.ExplosaoDir(i,j,1,0,1,6,matrizObjetos,dic, Raio)
		
		# Leste 
		self.ExplosaoDir(i,j,0,1,2,7,matrizObjetos,dic, Raio)
		
		# Oeste 
		self.ExplosaoDir(i,j,0,-1,3,8,matrizObjetos,dic, Raio)
		
	# Cria Explosao em um Raio de Alcance num direcao
	def ExplosaoDir(self,i,j,inch,incd,cauda,corpo,matrizObjetos,dic, Raio):
		
		h = i + inch
		d = j + incd
		inc = 0
		
		while( inc < Raio ) :
			
			if( matrizObjetos[h][d][0] != None or matrizObjetos[h][d][4] != None or  matrizObjetos[h][d][3] != None):
				# Se encontrar um Tijolo, destroi o tijolo e interrompe a criacao de novas explosoes
				
				if(matrizObjetos[h][d][4] != None):
					
					matrizObjetos[h][d][4].listaMetodosAnimacao[0] = True
					matrizObjetos[h][d][4].listaMetodosAcao[0] = True
					self.geriTijolo(h,d,matrizObjetos[h][d][4],matrizObjetos,dic)
					
				if(matrizObjetos[h][d][3] != None):
					
					ra = matrizObjetos[h][d][3].RaioAlcance
					matrizObjetos[h][d][3] = None
					
					# Cria Explosao
					self.criaExplosao(h,d,matrizObjetos,dic,ra)					
			
				inc = Raio
			
			elif(matrizObjetos[h][d][2] == None ):
				
				pos = matrizObjetos[h][d][1].getPosicao()
				matrizObjetos[h][d][2] = Explosao(dic['E'][7], dic['E'][0], pos, int (dic['E'][5]),int (dic['E'][6]), int (dic['E'][2]),int (dic['E'][3]))
				
				if(inc < Raio-1):
					
					matrizObjetos[h][d][2].SetTipoExplosao(corpo)
					
				else:
				
					matrizObjetos[h][d][2].SetTipoExplosao(cauda)
					
				
			h = h + inch
			d = d + incd
				
			inc = inc + 1
