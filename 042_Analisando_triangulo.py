# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# 	- EQUILÁTERO: todos os lados iguais
# 	- ISÓSCELES: dois lados iguais, um diferente
#	- ESCALENO: todos os lados diferentes

print()
l1 = float(input("1º seguimento: "))
l2 = float(input("2º seguimento: "))
l3 = float(input("3º seguimento: "))
print()
if (((l1+l2)>l3) and ((l1+l3)>l2) and ((l2+l3)>l1)):
	if (l1 == l2 == l3):
		print(f"Os segumentos {l1}, {l2} e {l3} formam um triângulo equilátero")
	elif ((l1 == l2) or (l2 == l3) or (l3 == l1)):
		print(f"Os segumentos {l1}, {l2} e {l3} formam um triângulo isósceles")
	else:
		print(f"Os segumentos {l1}, {l2} e {l3} formam um triângulo escaleno")
else:
	print(f"Os seguimentos {l1}, {l2} e {l3} não podem formar um triângulo.")
print()