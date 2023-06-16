# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import datetime

print()
ano = int(input("Qual ano deseja saber? "))
# ano = datetime.now().year

if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)):
	print(f"O ano {ano} é bissexto!")
else:
	print(f"O ano {ano} NÃO é bissexto!")
print()