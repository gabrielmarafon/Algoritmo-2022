matriz = [[0, 0], [0, 0]]
matriz2 = [[0, 0], [0, 0]]
maior = 0

for i in range(2):
  for j in range(2):
    numero = int(input(f'Digite um número:\n'))

    matriz[i][j] = numero

    if numero > maior:
      maior = numero

for k in range(2):
  for l in range(2):
    matriz2[k][l] = matriz[k][l] * maior

print(f'\n{matriz2}')