# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print()

sexo = str(input("Informe seu sexo (M/F): ")).strip().upper()[0]
print()
while sexo not in "MF":
	print("Dados INVÁLIDOS!")
	sexo = str(input("Informe seu sexo (M/F): ")).strip().upper()[0]
	print()

if (sexo == "M"):
	print("Sexo MASCULINO (XY) registrado com sucesso!")
else:
	print("Sexo FEMININO (XX) registrado com sucesso!")
	
print()