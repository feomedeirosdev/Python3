# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print()
nome = str(input("Digite seu nome completo: ")).strip().upper().split()
print()
print(nome)
print(f"{nome[0].capitalize()} {nome[-1].capitalize()}")
print()
