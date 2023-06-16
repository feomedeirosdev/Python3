# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print()
l_peso = []
for i in range(1, 6):
	peso = float(input(f"Peso(kg) da {i}º pessoa: "))
	l_peso.append(peso)
print()
print(l_peso)
maior = menor = l_peso[0]
for i in l_peso:
	if (i < menor):
		menor = i
	if (i > maior):
		maior = i
print()
print(f"Menor: {menor}")
print(f"Maior: {maior}")
print()