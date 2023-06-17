#  Crie um programa que leia dois valores e mostre um menu na tela:
# 	[ 1 ] somar
# 	[ 2 ] multiplicar
# 	[ 3 ] maior
# 	[ 4 ] novos números
# 	[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print()
# Validando se é número
v1 = str(input("1º valor: "))
while not v1.isdigit() :
	print()
	print("Entrada INVÁLIDA")
	v1 = str(input("1º valor: "))
v1 = int(v1)
# validando se é número
v2 = str(input("2º valor: "))
while not v2.isdigit():
	print()
	print("Entrada INVÁLIDA")
	v2 = str(input("2º valor: "))
v2 = int(v2)
print()

opc = ""
while opc != "x":
	print("Qual operação deseja realizar?")
	print("[1] Somar")
	print("[2] Multiplicar")
	print("[3] Maior")
	print("[4] Novos números")
	print("[x] Somar")
	opc = str(input(">>> "))
	if (opc == "1"):
		print(f"Soma: {v1} + {v2} = {v1+v2}")
	elif (opc == "2"):
		print(f"Produto: {v1} x {v2} = {v1*v2}")
	elif (opc == "3"):
		if (v1 > v2):
			print(f"{v1} é maior que {v2}")
		elif (v2 > v1):
			print(f"{v2} é maior que {v1}")
		else:
			print(f"{v1} e {v2} são iguais")
	elif (opc == "4"):
		# Validando se é número
		v1 = str(input("1º valor: "))
		while not v1.isdigit() :
			print("Entrada INVÁLIDA")
			v1 = str(input("1º valor: "))
		v1 = int(v1)
		# validando se é número
		v2 = str(input("2º valor: "))
		while not v2.isdigit():
			print("Entrada INVÁLIDA")
			v2 = str(input("2º valor: "))
		v2 = int(v2)
	else:
		print("Opção inválida")
	print()
print("Fim do programa")
print()


