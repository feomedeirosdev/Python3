# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print()
vel = float(input("Leitura de Velocidade (km/h): "))

if (vel <= 80):
	print("Siga com segurança!")
else:
	multa = (vel - 80) * 7
	print(f"Sua velocidade está {vel - 80} km/h acima do limite permitido.")
	print(f"Sua multa será de R$ {(multa):.2f}.")
print()