# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print()

l_nome = []
l_idade = []
l_sexo = []
NHMV = '' # Nome Homem Mais Velho
IHMV = 0 # Idade Homem Mais Velho
QMMV = 0 # Quantidade Mulheres Menores Vinte

for i in range(1, 5):
	nome = str(input("Nome: ")).capitalize()
	l_nome.append(nome)
	idade = int(input("Idade: "))
	l_idade.append(idade)
	sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
	l_sexo.append(sexo)
	# Encontrando o nome do homem mais velho
	if (sexo == "M" and idade > IHMV):
		IHMV = idade
		NHMV = nome
	# Contando as mulheres com menos de 20 anos
	if (sexo == "F" and idade < 20):
		QMMV += 1
	print()
print()
# Calculando a média de idade
med_idade = sum(l_idade) / len(l_idade)
print(f"A média das idades é {med_idade:.1f} anos")
if (IHMV != 0 and NHMV != ''):
	print(f"O nome do homem mais velho é {NHMV} com {IHMV} anos")
if (QMMV != 0):
	print(f"{QMMV} mulheres tem menos de 20 anos")
print()