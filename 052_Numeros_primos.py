# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print()
num = int(input("Digite o número: "))
print()
cont = 0
if(num==1):
	print("Por definição matemática o número 1 NÃO é considerado um número primo!")
else:
	for i in range(1, num+1):
		if(num%i==0):
			print(i)
			cont += 1

if(num!=1):
	if(cont==2):
		print(f"O número {num} foi dividido apenas {cont} vezes, portanto ele é primo")
	else:
		print(f"O número {num} foi dividido {cont} vezes, logo ele NÃO é primo!")

print()