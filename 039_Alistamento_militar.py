#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print()
ano_atual = date.today().year
ano_nasc = int(input("Qual é o ano de nascimento? "))
idade = ano_atual - ano_nasc
print()
if (idade < 18):
	print(f"Você tem {idade} anos e seu alistamento militar será daqui a {18-idade} anos em {ano_atual+(18-idade)}")
elif (idade == 18):
	print(f"Você tem {idade} anos e deve se alistar imediatamente")
else:
	print(f"Voce tem {idade} anos e seu alistamento deveria ter sido feito à {idade-18} anos em {ano_atual-(idade-18)}")
print()