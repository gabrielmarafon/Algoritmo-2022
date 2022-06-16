!pip install simple-colors

from simple_colors import *


opcoes = [
{
    'cod': 1,
    'metodo': 'Dinamite',
},
{
    'cod': 2,
    'metodo': 'Minhocas Radioativas',
},
{
    'cod': 3,
    'metodo': 'Retroescavadeira',
},
{
    'cod': 4,
    'metodo': 'Empurradores',
},
{
    'cod': 5,
    'metodo': 'Imãs',
},
{
    'cod': 6,
    'metodo': 'Fiat Uno de Firma',
},
{
    'cod': 7,
    'metodo': 'peixinhos',
},
{
    'cod': 8,
    'metodo': 'rebocadores',
},
{
    'cod': 9,
    'metodo': 'Noé',
},                 
]

sair = False


while sair == False:
  print(blue("********************************Operação Suez********************************"))
  print(yellow("-Detectamos nos nossos sistemas que o navio atingiu um grande banco de areia em uma das margens, encalhando o navio. Você tem limite de 6,5mi."))
  print(yellow("O que deseja fazer? Opções:\n1-Usar dinamite para fazer o banco de areia ceder(R$100.000,00).\n2-Usar minhocas biologicamente modifcadas para comer a areia(R$2mi)\n3-Usar retroescavadeiras para mover a areia para outro lugar(R$20.000,00)\n"))
  nivel_de_areia = 150
  verificacao = nivel_de_areia  
  escolha = int(input()) 
  for i in opcoes:
    if escolha == i['cod']:
       opcao = i
  if escolha > 3:  
    print(red('Opção inválida!'))

  if escolha == 1:
    print(green('Muito bem! Você tomou a melhor decisão.', 'bold',))
    sair = True          
    print("Detectamos nos nossos sistemas que existe um grande banco de areia com aproximadamente 150cm de profundidade, precisamos fazer com que ele chegue a 0.\nPrecisamos colocar as dinamites gradualmente para que não atinga o casco do barco. Quantas deseja usar?\n")   
    print(f'Nivel de areia restante: {nivel_de_areia}cm')
    while nivel_de_areia > 0:
      dinamite = int(input())
      if dinamite < 0:
        print(red('Opção inválida!'))
        sair = False
        correto = False
        break
      if dinamite > 5:
        print(red("Você atingiu o casco do navio."))
        sair = False
        correto = False
        break
      else: 
        nivel_de_areia = nivel_de_areia - (dinamite*5)
        print(f'Nivel de areia restante: {nivel_de_areia}cm')
      if nivel_de_areia <= 0:
        
        print(green("Parabéns! Conseguimos tirar o banco de areia. Agora precisamos fazer com que ele volte a sua posição original para seguir caminho."))
        for i in opcoes:
          if escolha == i['cod']:
            opcao = i
            correto = False
            print(yellow("Qual será sua próxima decisão?\n\n4- Usar imãs gigantes.\n5- Usar empurradores.\n6- Amarrar um Fiat Uno Mile Fire 2002 Álcool de firma com escada de aluminio para tirar o navio do canal(R$11.200,00 + 6,550 por litro).")) 
            escolha = int(input())
          if escolha == 4:
            print(red('Ta assistindo muito velozes e furiosos.'))
            sair = False
            break
          if escolha == 5:
            print(green('Parabéns! Certamente você tomou a decisão correta.'))
            correto = True
            break  
          if escolha == 6:
            sair = False
            print(red("Opção inviavel devido ao alto custo do Álcool e a dificuldade de encontrar um uno no deserto."))
            break
          if escolha < 4 or escolha > 6:  
            print(red('Opção inválida!'))
            sair = False
  
  while correto ==  True:
    for i in opcoes:
      if escolha == i['cod']:
        opcao = i
        print(yellow("-Conseguimos centralizar o navio. Agora precisamos fazer com que ele volte a navegar, decida o que vamos fazer agora."))
        print(yellow("\n7- 350 peixinhos dourados amarrados no navio.(R$10.000)\n8- Usar rebocadores para tracionar o navio, fazendo com que ele pegue no tranco.\n9- Aguardar o dilúvio.(120000 anos).\n"))    
          
    escolha = int(input())
    if escolha == 7:
      print(red("Provavelmente você terá problemas com Ibama, aguarde o processo."))
      sair = False
      correto = False
      break
      
    if escolha == 8:
      print(green("Parábens! Você não ferrou com a economia mundial."))
      sair = False
      correto = False
      
    if escolha == 9:
      print(red("Genênis 7:17 - Quarenta dias durou o Dilúvio, e as águas aumentaram e elevaram a arca acima da terra."))
      correto = False
      sair = False
      
      break
    if escolha > 9:  
      print(red('Opção inválida!'))
      sair = False
      break
  if escolha == 2:
    print(red('Incorreta! Volte para o 6º ano.', 'bold'))
    correto = False
  
  if escolha == 3:
    print(red('No ano de 2077 o serviço foi terminado. Parabéns pelos netos.', 'bold'))
    correto = False