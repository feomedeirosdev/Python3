# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 	- O nome com todas as letras maiúsculas e minúsculas.
# 	- Quantas letras ao todo (sem considerar espaços).
# 	- Quantas letras tem o primeiro nome.

print("")
nome = str(input("Digite seu nome completo: ")).strip()
print("")

print(f"{nome.upper()}")
print(f"{nome.lower()}")
print("")
print(f"{len(nome) - nome.count(' ')}")
nome_lista = nome.split()
print(nome_lista[0])
print(len(nome_lista[0]))
print(f"{nome.find(' ')}")
print("")
