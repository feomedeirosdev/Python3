# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print()
val_casa = float(input("Qual o valor total do imóvel? R$ "))
sal = float(input("Qual o salário do comprador? R$ "))
tempo = int(input("Em quantos anos pretente pagar? R$ "))
print()
if ((val_casa / (tempo * 12)) >= (0.3 * sal)):
	print("Não poderemos financiar a casa")
else:
	print("Seu empŕestimo foi aprovado!")
print()