# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("")
l1 = float(input("Lançe o comprimento (cm) do 1º segmento: "))
l2 = float(input("Lançe o comprimento (cm) do 2º segmento: "))
l3 = float(input("Lançe o comprimento (cm) do 3º segmento: "))
print("")

if ((l1+l2 > l3) and (l2+l3 > l1) and (l1+l3 > l2)):
	print(f"Os lados {l1}, {l2} e {l3} podem formar um triângulo")
else:
	print(f"Os lados {l1}, {l2} e {l3} NÃO podem formar um triângulo")
print("")