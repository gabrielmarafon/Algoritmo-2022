# primeiro indice é a linha, segundo a coluna
import random

# Variáveis

perguntas_iniciciais_validas = False

qtd_jogadores = 0
dificuldade = 0
config_dificuldade = {}

altura_tabuleiro = 10
largura_tabuleiro = 10

tabuleiro1 = []
tabuleiro2 = []

tabuleiro_jogador1 = []
tabuleiro_jogador2 = []

pontuacao_jogador_1 = 0
pontuacao_jogador_2 = 0

# Funções

def print_tabuleiro_jogador(jogador):
	print('')

	for i in range(largura_tabuleiro):
		if largura_tabuleiro == 10:
			if i == 0:
				print(f'   {i}', end="  ",),
			else:
				print(i, end="  ",),
		else:
			if i == 0:
				print(f'   {i}', end="  ",),
			elif i > 9:
				print(i, end=" ",)
			else:
				print(i, end="  ",),

	print('')

	if(jogador == 1):
		for i, line in enumerate(tabuleiro_jogador1):
			if i < 10:
				print(f' {i}', end=' ')
			else:
				print(i, end=' ')

			print('  '.join(map(str, line)))
	else:
		for i, line in enumerate(tabuleiro_jogador2):
			if i < 10:
				print(f' {i}', end=' ')
			else:
				print(i, end=' ')

			print ('  '.join(map(str, line)))

def preencher_bombas(nro_jogadores):
	quantidade_bombas = config_dificuldade['qtd_bombas']
	bombas_no_campo = 0

	while quantidade_bombas != bombas_no_campo:
		linha = random.randint(0, altura_tabuleiro - 1)		
		coluna = random.randint(0, largura_tabuleiro - 1)

		posicao_tabuleiro = tabuleiro1[linha][coluna]

		if posicao_tabuleiro != 'B' and posicao_tabuleiro != 'N':
			tabuleiro1[linha][coluna] = 'B'
			bombas_no_campo += 1

	if nro_jogadores == 2:
		bombas_no_campo = 0

		while quantidade_bombas != bombas_no_campo:
			linha = random.randint(0, altura_tabuleiro - 1)		
			coluna = random.randint(0, largura_tabuleiro - 1)

			if posicao_tabuleiro != 'B' and posicao_tabuleiro != 'N':
				tabuleiro2[linha][coluna] = 'B'
				bombas_no_campo += 1

def preencher_navios(nro_jogadores):
	quantidade_navios = config_dificuldade['qtd_navios']
	navios_no_campo = 0

	while quantidade_navios != navios_no_campo:
		coluna = random.randint(0, altura_tabuleiro - 1)		
		linha = random.randint(0, largura_tabuleiro - 1)

		posicao_tabuleiro = tabuleiro1[linha][coluna]
		ultima_coluna = (largura_tabuleiro - 1)

		if posicao_tabuleiro != 'N':
			if((coluna + 2) < ultima_coluna) and ((linha - 2) > 0):
				for v in range(2):
					tabuleiro1[linha][coluna + v] = 'N'
					
				navios_no_campo += 2

	if nro_jogadores == 2:
		navios_no_campo = 0

		while quantidade_navios != navios_no_campo:
			coluna = random.randint(0, altura_tabuleiro - 1)		
			linha = random.randint(0, largura_tabuleiro - 1)

			posicao_tabuleiro = tabuleiro2[linha][coluna]
			ultima_coluna = (largura_tabuleiro - 1)

			if posicao_tabuleiro != 'N':
				if((coluna + 2) < ultima_coluna) and ((linha - 2) > 0):
					for v in range(2):
						tabuleiro2[linha][coluna + v] = 'N'

					navios_no_campo += 2

def rodada_jogador1():
	pontuacao_jogador1 = 0
	rodada = True
	escolhendo_linha = True
	escolhendo_coluna = True
	jogada_valida = False
	nro_jogadas_validas = 0
	mensagem_final = 'Suas jogadas encerraram!'

	while rodada == True:
		while nro_jogadas_validas != config_dificuldade['nro_jogadas']:
			print_tabuleiro_jogador(1)

			jogada_valida = False		
			
			escolhendo_linha = True
			escolhendo_coluna = True

			posicao_linha = 0
			posicao_coluna = 0

			while jogada_valida == False:
				while escolhendo_coluna == True:
					posicao_coluna = int(input(f'\nEm qual coluna você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_coluna >= 0) and (posicao_coluna <= (altura_tabuleiro - 1)):
						escolhendo_coluna = False
					else:
						print('\nDigite um valor válido!')

				while escolhendo_linha == True:
					posicao_linha = int(input(f'\nEm qual linha você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_linha >= 0) and (posicao_linha <= (largura_tabuleiro - 1)):
						escolhendo_linha = False
					else:
						print('\nDigite um valor válido!\n')

				if(tabuleiro1[posicao_linha][posicao_coluna] != 'Ç'):
					if(tabuleiro1[posicao_linha][posicao_coluna] == 'N'):
						pontuacao_jogador1 += 10

						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'N'						

						nro_jogadas_validas += 1
						jogada_valida = True

					if(tabuleiro1[posicao_linha][posicao_coluna] == '-'):
						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'A'						

						nro_jogadas_validas += 1
						jogada_valida = True

					if (tabuleiro1[posicao_linha][posicao_coluna] == 'B'):
						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'B'
						
						mensagem_final = 'Você encontrou uma bomba!'
						jogada_valida = True
						nro_jogadas_validas = config_dificuldade['nro_jogadas']
						rodada = False				
				else:
					print('\nVocê já jogou nesta posição!')

					jogada_valida = False	
					escolhendo_linha = True
					escolhendo_coluna = True	
		
		print_tabuleiro_jogador(1)
		rodada = False

	print(f'\n{mensagem_final}')

	return pontuacao_jogador1

def rodada_jogador2():
	pontuacao_jogador2 = 0
	rodada = True
	escolhendo_linha = True
	escolhendo_coluna = True
	jogada_valida = False
	nro_jogadas_validas = 0
	mensagem_final = 'Suas jogadas encerraram!'

	while rodada == True:
		while nro_jogadas_validas != config_dificuldade['nro_jogadas']:
			print_tabuleiro_jogador(2)

			jogada_valida = False		
			
			escolhendo_linha = True
			escolhendo_coluna = True

			posicao_linha = 0
			posicao_coluna = 0

			while jogada_valida == False:
				while escolhendo_coluna == True:
					posicao_coluna = int(input(f'\nEm qual coluna você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_coluna >= 0) and (posicao_coluna <= (altura_tabuleiro - 1)):
						escolhendo_coluna = False
					else:
						print('\nDigite um valor válido!')

				while escolhendo_linha == True:
					posicao_linha = int(input(f'\nEm qual linha você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_linha >= 0) and (posicao_linha <= (largura_tabuleiro - 1)):
						escolhendo_linha = False
					else:
						print('\nDigite um valor válido!\n')

				if(tabuleiro2[posicao_linha][posicao_coluna] != 'Ç'):
					if(tabuleiro2[posicao_linha][posicao_coluna] == 'N'):
						pontuacao_jogador2 += 10

						tabuleiro2[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador2[posicao_linha][posicao_coluna] = 'N'						

						nro_jogadas_validas += 1
						jogada_valida = True

					if(tabuleiro2[posicao_linha][posicao_coluna] == '-'):
						tabuleiro2[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador2[posicao_linha][posicao_coluna] = 'A'						

						nro_jogadas_validas += 1
						jogada_valida = True

					if (tabuleiro2[posicao_linha][posicao_coluna] == 'B'):
						tabuleiro2[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador2[posicao_linha][posicao_coluna] = 'B'
						
						mensagem_final = 'Você encontrou uma bomba!'
						jogada_valida = True
						nro_jogadas_validas = config_dificuldade['nro_jogadas']
						rodada = False				
				else:
					print('\nVocê já jogou nesta posição!')

					jogada_valida = False	
					escolhendo_linha = True
					escolhendo_coluna = True	
		
		print_tabuleiro_jogador(2)
		rodada = False

	print(f'\n{mensagem_final}')

	return pontuacao_jogador2

def mostrar_resultado_final(nro_jogadores):
	print('\n=======================================')
	print('\nResultados da partida:')
	if nro_jogadores == 1:
		print(f'\nPontuação atingida: {pontuacao_jogador_1}')
	else:
		print(f'\nPontuação do jogador 1: {pontuacao_jogador_1}')
		print(f'Pontuação do jogador 2: {pontuacao_jogador_2}')

		if pontuacao_jogador_1 > pontuacao_jogador_2:
			print(f'\nJogador 1 é o campeão!')
		elif pontuacao_jogador_1 < pontuacao_jogador_2:
			print(f'\nJogador 2 é o campeão!')
		else:
			print(f'\nEmpate!')

	print('\n=======================================')
	
# Início

# Configuração inicial da partida
while perguntas_iniciciais_validas == False:
	while (qtd_jogadores == 0):
		resposta = int(input('Quantos jogadores irão jogar? (1/2)\n'))

		if (resposta == 1):
			qtd_jogadores = 1
		elif (resposta == 2):
			qtd_jogadores = 2	
		else:
			print('\nEntre com um valor válido!\n')

	while (dificuldade == 0):
		resposta = int(input('\nSelecione a dificuldade:\n 1- Normal\n 2- Difícil\n'))

		if (resposta == 1):
			dificuldade = 1

			config_dificuldade = {
				'qtd_bombas': 30,
				'qtd_navios': 20,
				'nro_jogadas': 10,
			}
		elif (resposta == 2):
			dificuldade = 2

			config_dificuldade = {
				'qtd_bombas': 100,
				'qtd_navios': 50,
				'nro_jogadas': 20,			
			}

			altura_tabuleiro = 20
			largura_tabuleiro = 20
		else:
			print('\nEntre com um valor válido!')

	perguntas_iniciciais_validas = True

# Gera a matriz dos tabuleiros com base no nro de jogadores
if(qtd_jogadores == 1):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	
	tabuleiro_jogador1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]	
elif(qtd_jogadores == 2):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	tabuleiro2 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]

	tabuleiro_jogador1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]	
	tabuleiro_jogador2 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]		

# Preenche os tabuleiros com bombas e navios 
preencher_navios(qtd_jogadores)
preencher_bombas(qtd_jogadores)

# Vez do jogador 1
pontuacao_jogador_1 = rodada_jogador1()

# Vez do jogador 2
if qtd_jogadores == 2:
	print('\nAgora é a vez do jogador 2!')
	pontuacao_jogador_2 = rodada_jogador2()

# Mostra oss resultados finais da partida
mostrar_resultado_final(qtd_jogadores)