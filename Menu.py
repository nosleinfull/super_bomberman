"""
Universidade Estadual de Mato Grosso do Sul
Topicos em Computacao I  Trabalho I

Autor:
Leandro Souza da Silva
Nielson Fernandes Silva

Data 2014
"""

"""
Classe que contem o Game Loop
"""

from Gestor_Inicializacao import *
import thread

#Pre Processa a matriz do Jogo para Renderizacao
def preProcessamentoImage(getMatrizObjetos, processadorGrafico):
	
	priori = []
	
	for i in range (len(matrizObjetos)):

		for j in range (len (matrizObjetos[0])):

			lis = matrizObjetos[i][j]

			for k in lis:

				if (k != None and k.getNome() != 'personagem'):
					
					image = k.getConjuntoImg()
					x = k.getIndexConjuntoImgX()
					y = k.getIndexConjuntoImgY()

					processadorGrafico.render2(image[x][y], k.posicao[0],k.posicao[1])

				elif(k != None and k.getNome() == 'personagem'):
					
					priori.append(k)
		
	for k in priori:
		
		if (k != None ):
			
			image = k.getConjuntoImg()
			x = k.getIndexConjuntoImgX()
			y = k.getIndexConjuntoImgY()
			processadorGrafico.render2(image[x][y],k.posicao[0],k.posicao[1])

def render(threadName, delay, arg1, arg2):

	#Aqui os objetos sao chamados para serem renderizados
	preProcessamentoImage(arg1, arg2)
	
	#Aqui atualiza o cenario como um todo
	processadorGrafico.updateScreen()


if __name__ == '__main__':

	#objetos e variaveis para o jogo
	
	# Carrega Cenario e todos os seus Objetos para o Jogo
	obj = ProcessadorInicialDeJogo("Cenario_1")
	matrizObjetos = obj.getMatrizObjetos()	
	gestorRegras = GestorRegras()
	dic = obj.getDic()

	#variavel que controla o loop do jogo
	running = True
	

	#Predefinicao do cenario a partir do mapa de caracteres
	larguraCenario = len(matrizObjetos[0])
	alturaCenario  = len(matrizObjetos)
	sizeObjLargura = matrizObjetos[0][0][0].getAlturaImg()
	sizeObjAltura  = matrizObjetos[0][0][0].getLarguraImg()

	#Define as coordenadas da tela, largura e altura e clock do jogo
	processadorGrafico = ProcessadorGrafico( larguraCenario*sizeObjLargura, alturaCenario*sizeObjAltura ,0)
	gestorEntrada = GestorEntrada()
	
	
	
	M = len(matrizObjetos)
	N = len (matrizObjetos[0])
	
	# Posteriormente sera aplicado o uso de concorrencia para melhor aproveitamento dos recursos de hardware
	while running:

		for i in range (M):
		
			for j in range (N):

				lis = matrizObjetos[i][j]
				l = 0
				comando = []
				gestorEntrada.getListaComandos(comando)
				for k in lis:
					
					if (k != None and k.getNome() == 'personagem'):
					
						comando1 = gestorEntrada.ajustaListaComandos(comando, k.ListaComandos)				
						gestorRegras.geriPersonagem(i, j, l,k, matrizObjetos, comando1, dic)

					elif (k != None and k.getNome() == 'bomba'):
						gestorRegras.geriBomba(i, j, k, matrizObjetos, dic)
					
					elif (k != None and k.getNome() == 'tijolo'):
						gestorRegras.geriTijolo(i, j,k, matrizObjetos, dic)

					elif(k != None and k.getNome() == 'explosao'):
						gestorRegras.geriExplosao(i, j, k, matrizObjetos, dic)
					l+=1			
					
				
		#Aqui os objetos sao chamados para serem renderizados
		preProcessamentoImage(matrizObjetos, processadorGrafico)
		
		#Aqui atualiza o cenario como um todo
		processadorGrafico.updateScreen()
		
		#thread.start_new_thread(render,("tr", 0, matrizObjetos, processadorGrafico))