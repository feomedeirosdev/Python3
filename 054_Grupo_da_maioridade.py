# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

ano_atual = datetime.now().year

lista = []
lidade = []

print()
for i in range(1, 8):
	ano_nasc = int(input(f"Qual é o ano de nascimento da {i}ª pessoa? "))
	lista.append(ano_nasc)
	idade = ano_atual - ano_nasc
	lidade.append(idade)
print()
print(lista)
print(lidade)
print()
maior = menor = 0
for i in lidade:
	print(i)
	if(i<18):
		menor += 1
	else:
		maior += 1
print(f"Ao todo foram {menor} pessoas menores de idade")
print(f"Ao todo foram {maior} pessoas maiores de idade")
print()
