# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.



print()
num = int(input("Digite um número inteiro: "))
print()
print("Para qual base numérica você deseja converter?")
print("[ 1 ] Binário")
print("[ 2 ] Octal")
print("[ 3 ] Hexadecimal")
esc = int(input("> "))
print()
if (esc == 1):
	print(f"{num} em binário é: {bin(num)[2:]}")
elif (esc == 2):
	print(f"{num} em octal é: {oct(num)[2:]}")
elif (esc == 3):
	print(f"{num} em hexadecimal é: {hex(num)[2:].upper()}")
else:
	print("Opção inválida!")
print()