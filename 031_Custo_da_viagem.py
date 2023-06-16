#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print()
dist = float(input("Qual é a distância (km/h) da viagem? "))
if (dist <= 200):
	custo = dist * 0.5
else:
	custo = dist * 0.45
print()
print(f"O custo total da viagem será de: R$ {(custo):.2f}.")
print()

#custo = (dist * 0.5) if (dist <= 200) else (dist * 0.45)