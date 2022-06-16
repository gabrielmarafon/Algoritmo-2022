from math import floor

valor = float(input())

moedas1real = floor(valor / 100)

moedasDe50Cent = floor((valor % 100) / 50)

moedasDe10Cent = floor((valor % 50) / 10)

moedasDe5Cent = floor((valor % 10) / 5)

moedasDe1Cent = floor((valor % 5) / 1)

print("Moedas de 1 real:", moedas1real)
print("Moedas de 50 centavos:", moedasDe50Cent)
print("Moedas de 10 centavos:", moedasDe10Cent)
print("Moedas de 5 centavos:", moedasDe5Cent)
print("Moedas de 1 centavos:", moedasDe1Cent)