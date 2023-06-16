#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print()
sal = float(input("Qual o salário do funcionário R$ "))
print()

if (sal > 1250):
	sal = 1.1 * sal
else:
	sal = 1.15 * sal

print(f"O novo salário é  R$ {(sal):.2f}")
print()