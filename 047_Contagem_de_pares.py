# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print()
li = int(input("Digite o limite inferior: "))
ls = int(input("Digite o limite superior: "))
print()
if (li%2==0):
	for i in range(li, ls+1, 2):
		print(i, end=" ")
else:
	for i in range(li+1, ls+1, 2):
		print(i, end=" ")
print()
print()