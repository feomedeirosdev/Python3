# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# 	- à vista dinheiro/cheque: 10% de desconto
# 	- à vista no cartão: 5% de desconto
# 	- em até 2x no cartão: preço formal
# 	- 3x ou mais no cartão: 20% de juros

print()
valor = float(input("Qual o valor total da compra? R$ "))
print()
print("Como deseja pagar?")
print("[1] à vista dinheiro (-10%)")
print("[2] à vista cartão (-5%)")
print("[3] em até 2x no cartão (s/ juros)")
print("[4] 3x ou mais vezes no cartão (+20%)")
esc = int(input("> "))
print()
if (esc == 1):
	valor = 0.9*valor
	print(f"Com desconto de 10% o total a pagar fica R$ {valor:.2f}")
elif (esc == 2):
	valor = 0.95*valor
	print(f"Com desconto de 5% o total a pagar fica R$ {valor:.2f}")
elif (esc == 3):
	print(f"O total a pagar fica R$ {valor:.2f}")
elif (esc == 4):
	valor = 1.2*valor
	print(f"Com acréssimo de 20% o total a pagar fica R$ {valor:.2f}")
else:
	print("Opção inválida")
print()
