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
Classe contendo os objetos do Jogo
"""

class Objeto():

	def __init__(self, conjuntoImg = None, nome = None, posicao = [0,0], laguraImg = 0, alturaImg = 0 ):

		self.conjuntoImg = conjuntoImg
		self.indexConjuntoImgX = 0
		self.indexConjuntoImgY = 0
		self.laguraImg = laguraImg
		self.alturaImg = alturaImg
		self.nome = nome
		self.posicao = posicao


	def getLarguraImg(self):
		return self.laguraImg


	def getAlturaImg(self):
		return self.alturaImg

	def getIndexConjuntoImgX(self):

		return self.indexConjuntoImgX

	def getIndexConjuntoImgY(self):
		
		return self.indexConjuntoImgY	


	def getConjuntoImg(self):
	
		return self.conjuntoImg

	def getNome (self):
		
		return self.nome

	def getPosicao(self):

		return self.posicao

	def setConjuntoImg(self, conjuntoImg):			

		self._conjuntoImg = conjuntoImg

	def setNome(self, nome):

		self.nome = nome

	def setPosicao(self, x, y):

		self._posicao[0] = x
		self._posicao[1] = y



"""
classe base passra os demais  objetos animados
"""

class ObjetoAnimado(Objeto):

	def __init__(self, conjuntoImg = None, nome = None, posicao = [0,0] ,  limMudEstado = 0, tempoDuracaoFrames = 0, laguraImg = 0, alturaImg = 0):

		Objeto.__init__(self, conjuntoImg, nome, posicao, laguraImg , alturaImg )

		self.estado = 1
		self.limMudEstado = limMudEstado
		self.sensor = []
		self.tempoDuracaoFrames = tempoDuracaoFrames


	def animaAcao(self, tipo):
		pass
		#metodo base para ser sobrecarregado

	def acao(self, tipo):
		#metod base para ser sobrecarregado
		pass

	def getEstado(self):
		return self.estado

	def getSensor(self):	
		return self.sensor

	def getlimMudEstado(self):
		return self.limMudEstado

	def getTempoDuracaoFrames(self):
		return self.TempoDuracaoFrames

	def getIncFrameEstado(self):
		return self.incFrameEstado		

	def setEstado(self, estado):
		self.estado = estado

	def setIncFrameEstado(self, incFrameEstado):
		self.incFrameEstado = incFrameEstado

	def setlimMudEstado(self, limMudEstado):
		self.limMudEstado = limMudEstado


	def TempoDuracaoFrames(self, tempoDuracaoFrames):
		self.tempoDuracaoFrames = tempoDuracaoFrames


	def setSensor(self, sensor):
		self.sensor = sensor

class Tijolos(ObjetoAnimado):


	def __init__(self, conjuntoImg = None, nome = None, posicao = [0,0],  limMudEstado = 0, tempoDuracaoFrames = 0, laguraImg = 0, alturaImg = 0 ):

		ObjetoAnimado.__init__(self, conjuntoImg, nome, posicao, limMudEstado, tempoDuracaoFrames, laguraImg , alturaImg )

		self.listaMetodosAnimacao = [False]
		self.listaMetodosAcao = [False]
		self.incFrameEstadoAnimacaoTipo1 = 0
		self.incFrameEstadoAcao1 = 0	

	def animaAcao(self, tipo):

		if (tipo == 1):

			self.__animaAcao1()


	def acao(self, tipo):

		if (tipo == 1):
			self.__acao1()

	#implementa animaca do tijolo morrendo  do tipo 1
	def __animaAcao1(self):


		self.incFrameEstadoAnimacaoTipo1 += 1

		if (self.incFrameEstadoAnimacaoTipo1 % self.limMudEstado == 0):

			self.indexConjuntoImgY += 1

			if (self.indexConjuntoImgY == len(self.conjuntoImg[0])):

				self.indexConjuntoImgY = 0
				self.indexConjuntoImgX +=1


				if (self.indexConjuntoImgX == len(self.conjuntoImg)):
			
					self.indexConjuntoImgX = 0


		if (self.incFrameEstadoAnimacaoTipo1 == self.tempoDuracaoFrames):

			self.listaMetodosAnimacao[0] = True
			self.incFrameEstadoAnimacaoTipo1 = 0
						
			
	#implementa acao de incrementar a variavel incFrameEstado para animacao do tipo 1
	def __acao1(self):
		
		self.incFrameEstadoAcao1 +=1

		if (self.incFrameEstadoAcao1 == self.tempoDuracaoFrames):
			self.incFrameEstadoAcao1 = 0
			self.listaMetodosAcao[0] = False
			self.estado = 0

class Explosao(ObjetoAnimado):

	# Construtor que Contem os atributos da classe Pai
	def __init__(self,ConjuntoImg = None, Nome = None, Posicao = [0,0] , limMudEstado = 0, tempoDuracaoFrames = 0, larguraImg = 0, alturaImg = 0):
		
		# Inicializando os atributos da classe Pai
		ObjetoAnimado.__init__(self, ConjuntoImg, Nome, Posicao, limMudEstado, tempoDuracaoFrames,larguraImg, alturaImg)
		
		self.IncFrameEstado = 0
		self.inc = 1
		self.incVida = 0
		
		self.listaMetodosAnimacao = [False,False]

	def SetTipoExplosao(self,Tipo):
	
		self.indexConjuntoImgX = Tipo
		
	def AnimaExplodir(self):
	
		self.IncFrameEstado = self.IncFrameEstado + 1
		
		if( self.IncFrameEstado % self.limMudEstado == 0):
		
			if( self.indexConjuntoImgY == 3 ):
			
				self.inc = -1
				
			if( self.indexConjuntoImgY == 0 ):
			
				self.inc = 1			
			self.indexConjuntoImgY = self.indexConjuntoImgY + self.inc
			
		
		# Se a animacao acabar
		if( self.IncFrameEstado == self.tempoDuracaoFrames):

			self.IncFrameEstado = 0
			self.listaMetodosAnimacao[0] = False

	def AcaoExplodir(self):
		
		self.incVida = self.incVida + 1
		if( self.incVida == self.tempoDuracaoFrames ):
		
			# Estado do Objeto Morto, Pronto para ser destruido
			self.incVida = 0
			self.estado = 0

	# Overriding
	def AnimaAcao(self, Tipo):

		self.AnimaExplodir()

	# Overriding
	def Acao(self, Tipo):

		self.AcaoExplodir()
		
	def SetIncVida(self, IncVida):
		
		self.IncVida = IncVida

class Poderes(ObjetoAnimado):

	def __init__(self,ConjuntoImg = None, Nome = None, Posicao = [0,0] , limMudEstado = 0, tempoDuracaoFrames = 0, larguraImg = 0, alturaImg = 0,Tipo = 0):
		
		ObjetoAnimado.__init__(self, ConjuntoImg, Nome, Posicao, limMudEstado, tempoDuracaoFrames,larguraImg, alturaImg)
		self.TipoPoder = Tipo
		self.IndexConjuntoImgX = Tipo
		
		self.IncAnimaPoder = 0
		self.IncAnimaQueimar = 0
		self.incPoder = 1
		self.incQueimar = 1
		self.incVida = 0
		
		self.listaMetodosAnimacao = [False,False]
		self.ListaMetodosAcao = [False]

	def AnimaPoder(self):
			
		self.IncAnimaPoder = self.IncAnimaPoder + 1
		
		if( self.IncAnimaPoder == (2*self.limMudEstado) ):
		
			if( self.indexConjuntoImgY >= 4 ):
				
				self.indexConjuntoImgY = 4
				self.incPoder = -1
				
			if( self.indexConjuntoImgY == 0 ):
			
				self.incPoder = 1
				
			self.indexConjuntoImgY = self.indexConjuntoImgY + self.incPoder
			self.IndexConjuntoImgX = self.TipoPoder
		
			self.IncAnimaPoder = 0
			self.listaMetodosAnimacao[0] = False

	def AnimaQueimar(self):
		
		if( self.incAnimaQueimar == 0 and self.indexConjuntoImgY != 0):
		
			self.indexConjuntoImgY = 0
		
		self.IncAnimaQueimar = self.IncAnimaQueimar + 1
		
		if( self.IncAnimaQueimar % self.limMudEstado == 0):
		
			if( self.indexConjuntoImgY == 9 ):
			
				self.incQueimar = -1
				
			if( self.indexConjuntoImgY == 0 ):
			
				self.incQueimar = 1
				
			self.indexConjuntoImgY = self.indexConjuntoImgY + self.incQueimar
			self.IndexConjuntoImgX = 0
		
		# Se a animacao acabar
		if( self.IncAnimaQueimar == self.tempoDuracaoFrames ):

			self.IncAnimaQueimar = 0
			self.listaMetodosAnimacao[1] = False

	def AcaoQueimar(self):
		
		self.incVida = self.incVida + 1
		if( self.incVida == self.tempoDuracaoFrames ):
		
			# Estado do Objeto Morto, Pronto para ser destruido
			self.incVida = 0
			self.Estado = 0
			self.ListaMetodosAcao[0] = False
			
			
	def GetTipoPoder(self):
	
		return TipoPoder()
		
	def SetTipoPoder(self, Tipo):
	
		self.TipoPoder = Tipo
		self.indexConjuntoImgY = Tipo
	
	def AnimaAcao(self, Tipo):
		
		if(Tipo == 0):
			
			self.AnimaPoder()
			
		if(Tipo == 1):
		
			self.AnimaQueimar()
			
	def Acao(self, Tipo):
	
		self.AcaoQueimar()
	
	def SetIncVida(self, IncVida):
		
		self.IncVida = IncVida	

class Bomba(ObjetoAnimado):

	def __init__(self,ConjuntoImg = None, Nome = None, Posicao = [0,0] , limMudEstado = 0, tempoDuracaoFrames = 0, larguraImg = 0, alturaImg = 0, RaioAlcance = 0):
		
		ObjetoAnimado.__init__(self, ConjuntoImg, Nome, Posicao, limMudEstado, tempoDuracaoFrames,larguraImg, alturaImg)
		
		# Movimento Inativo
		self.EstadoMovimento = 0
		
		# Raio de Alcance da Bomba
		self.RaioAlcance = RaioAlcance
		
		self.IncFrameEstado = 0
		self.inc = 1
		self.incVida = 0
		
		self.listaMetodosAnimacao = [False]
		
		# Tamanho em Pixel do movimento da Bomba
		self.mov = 8
		
	def AnimaBomba(self):
		
		self.IncFrameEstado = self.IncFrameEstado + 1
		
		if( self.IncFrameEstado % self.limMudEstado == 0):
		
			if(self.indexConjuntoImgY == 2):
				
				self.inc = -1
				
			if(self.indexConjuntoImgY == 0):
			
				self.inc = 1
				
			self.indexConjuntoImgY = self.indexConjuntoImgY + self.inc
			self.IndexConjuntoImgX = 0
		
		if(self.IncFrameEstado == self.tempoDuracaoFrames ):
			
			self.IncFrameEstado = 0
			self.listaMetodosAnimacao[0] = False
				
	def AcaoMover(self, Tipo):
	
		# Norte
		if(Tipo == 0):
			
			self.posicao[1] = self.posicao[1] + self.mov
			
		# Sul
		if(Tipo == 1):
		
			self.posicao[1] = self.posicao[1] - self.mov
			
		# Leste
		if(Tipo == 2):
		
			self.posicao[0] = self.posicao[0] + self.mov
		
		#Oeste
		if(Tipo == 3):
		
			self.posicao[0] = self.posicao[0] - self.mov
	
	def AcaoTempoBomba(self):
	
		self.incVida = self.incVida + 1
		if(self.incVida == self.tempoDuracaoFrames):
			
			self.incVida = 0
			self.estado  = 0

	def GetEstadoMovimento(self):
	
		return self.EstadoMovimento

	def SetEstadoMovimento(self, Estado):
	
		if( Estado == 0 or Estado == 1):
		
			self.EstadoMovimento = Estado

	# Overriding
	def AnimaAcao(self, Tipo):

		self.AnimaBomba()

	# Overriding
	def Acao(self, Tipo):
		
		if(Tipo >= 0 and Tipo <= 3):
		
			self.AcaoMover(Tipo)
			
		if(Tipo == 4):
		
			self.AcaoTempoBomba()

	def SetIncVida(self, IncVida):
		
		self.IncVida = IncVida

class Personagem(ObjetoAnimado):

	def __init__(self,ConjuntoImg = None, Nome = None, Posicao = [0,0] , limMudEstado = 0, tempoDuracaoFrames = 0, larguraImg = 0, alturaImg = 0, listaComandos = None):
	
		ObjetoAnimado.__init__(self, ConjuntoImg, Nome, Posicao, limMudEstado, tempoDuracaoFrames,larguraImg, alturaImg)
		
		# Lista de Poderes do Personagem, Livre para o Processador de Regras
		self.ListaPoder = [0,0,0,0,0,0,0,0]
		
		# Lista de Comandos do Personagem, Livre para o Processador de Regras
		self.ListaComandos = listaComandos
		
		self.listaMetodosAnimacao = [False, False]
		self.listaMetodosAcao = [False]
		
		self.IncMovimento = 0
		self.IncMorrer = 0
		self.IncVida = 0
		
		self.mov = 4

		self.animation = None
		
		# Index de Animacao de Movimento, Guarda o valor da ultima animacao de movimento
		self.IndexMovY = 0
		self.IndexMovX = 0
		
		# Index Animacao Morte, Guarda o valor da ultima animacao de morte
		self.IndexMorteY = 0
		self.IndexMorteX = 0
	

	def getListaComandos(self):
		return self.ListaComandos

	def AnimaMover(self, Tipo):
		
		self.indexConjuntoImgX = Tipo
		self.IncMovimento = self.IncMovimento + 1
		
		if( self.IncMovimento == self.limMudEstado ):
			
			
			if(self.IndexMovY == 10):
				
				self.IndexMovY = 0
			
			self.IndexMovY = self.IndexMovY + 1			
			
			self.indexConjuntoImgY = self.IndexMovY

			self.IndexMovX = Tipo
		
			
			
			self.IncMovimento = 0
			self.listaMetodosAnimacao[0] = False

	def AnimaMorrer(self):
				
		self.IncMorrer = self.IncMorrer + 1
		
		if( self.IncMorrer % self.limMudEstado == 0):
			
			self.IndexMorteY = self.IndexMorteY + 1
			self.indexConjuntoImgY = self.IndexMorteY
			self.indexConjuntoImgX = 4
			
		# Se a animacao acabar
		if( self.IncMorrer == 24):
			
			self.IndexMorteY = 0
			self.IncMorrer = 0
			self.listaMetodosAnimacao[1] = False
	
	def AnimaParado(self):
		self.IncMovimento = 0
		self.indexConjuntoImgY = 0
		#self.indexConjuntoImgX = self.IndexMovX
		#print " X", self.indexConjuntoImgX


	def AcaoMover(self, Tipo):
	
		# Norte
		if(Tipo == 0):
			
			self.posicao[1] = self.posicao[1] - (self.mov + self.ListaPoder[1])
			
		# Sul
		if(Tipo == 1):
		
			self.posicao[1] = self.posicao[1] + (self.mov + self.ListaPoder[1])
			
		# Leste
		if(Tipo == 2):
		
			self.posicao[0] = self.posicao[0] + (self.mov + self.ListaPoder[1])
		
		#Oeste
		if(Tipo == 3):
		
			self.posicao[0] = self.posicao[0] - (self.mov + self.ListaPoder[1])

	def AcaoMorrer(self):
		
		self.IncVida = self.IncVida + 1
		if(self.IncVida == self.tempoDuracaoFrames):
			
			self.IncVida = 0
			self.estado = 0
			self.listaMetodosAcao[0] = False

	def SetIncVida(self, IncVida):
		
		self.IncVida = IncVida

	def Acao(self, Tipo):
		
		if(Tipo >= 0 and Tipo <= 3):
		
			self.AcaoMover(Tipo)
			
		if(Tipo == 4):
		
			self.AcaoMorrer()
			
	def AnimaAcao(self, Tipo):
	
		if(Tipo >= 0 and Tipo <= 3):
		
			self.AnimaMover(Tipo)

		if(Tipo == 4):			
			self.AnimaMorrer()
		
		if(Tipo == 5):

			self.AnimaParado()	

if __name__ == '__main__':

	obj = Tijolos("Teste", "Player-1", [20,20], 2, 4)
	obj.animaAcao(1)
	#print obj.nome()