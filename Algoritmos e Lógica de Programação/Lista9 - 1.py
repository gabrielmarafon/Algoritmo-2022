def primo(n):
  for val in range(2,n):
    if n % val == 0:
      return False

  return True

numeros = []