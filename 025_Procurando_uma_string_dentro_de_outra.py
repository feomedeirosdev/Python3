#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print()
nome = str(input("Entre com seu nome: ")).strip().upper().split()
print()
print(nome)
print("SILVA" in nome)
print()