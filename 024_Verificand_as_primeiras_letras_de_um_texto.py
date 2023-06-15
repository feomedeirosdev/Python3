# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

print()
cidade = str(input("Digite o nome da sua cidade: ")).strip().upper().split()
print()
print(cidade[0] == "SANTO")
print()