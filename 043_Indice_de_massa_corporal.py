# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# 	- IMC abaixo de 18,5: Abaixo do Peso
# 	- Entre 18,5 e 25: Peso Ideal
# 	- 25 até 30: Sobrepeso
# 	- 30 até 40: Obesidade
# 	- Acima de 40: Obesidade Mórbida

print()
peso = float(input("Qual a massa (kg) do paciente: "))
altura = float(input("Qual a altura (m) do paciente: "))
IMC = peso / (altura * altura)
print()
if (IMC <= 18.5):
	print(f"IMC: {IMC:.1f} - Abaixo do peso")
elif (18.5 < IMC <= 25):
	print(f"IMC: {IMC:.1f} - Peso ideal")
elif (25 < IMC <= 30):
	print(f"IMC: {IMC:.1f} - Sobrepeso")
elif (30 < IMC <= 40):
	print(f"IMC: {IMC:.1f} - Obesidade")
else:
	print(f"IMC: {IMC:.1f} - Obesidade Mórbida")
print()