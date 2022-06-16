import random

h, w = 10, 20
numeros = [[0 for x in range(w)] for y in range(h)]
produtos = [[0 for x in range(w)] for y in range(h)]
somas = []

for i in range(h):
  soma = 0
  
  for j in range(w):
    numeros[i][j] = random.randint(1, 10)
    soma += numeros[i][j] 
  
  somas.append(soma)

for k in range(h):
  for l in range(w):
    produtos[k][l] = numeros[k][l] * somas[k]

print(f'Matriz inicial:\n{numeros}')
print(f'\nSomas:\n{somas}')
print(f'\nMatriz resultante:\n{produtos}')