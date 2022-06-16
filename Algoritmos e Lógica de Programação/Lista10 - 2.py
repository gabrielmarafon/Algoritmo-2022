h, w = 10, 3
notas = [[0 for x in range(w)] for y in range(h)]

cont_menor_nota1 = 0
cont_menor_nota2 = 0
cont_menor_nota3 = 0

for i in range(h):
  for j in range(w):
    nota = float(input(f'Qual é a nota {j + 1} do aluno {i + 1}:\n'))

    notas[i][j] = nota

print('\nRelatório:\n')

for k in range(h):
  menor = 99999999999

  for l in range(w):
    if notas[k][l] < menor:
      menor = notas[k][l]

  if notas[k][0] < notas[k][1] and notas[k][0] < notas[k][2]:
    cont_menor_nota1 += 1
  elif notas[k][1] < notas[k][0] and notas[k][1] < notas[k][2]:
    cont_menor_nota2 += 1
  elif notas[k][2] < notas[k][0] and notas[k][2] < notas[k][1]: 
    cont_menor_nota3 += 1

  print(f'Aluno {k+1} - menor nota: {menor}')

print(f'\nQtd alunos com as menores notas na prova 1: {cont_menor_nota1}')
print(f'Qtd alunos com as menores notas na prova 2: {cont_menor_nota2}')
print(f'Qtd alunos com as menores notas na prova 3: {cont_menor_nota3}')