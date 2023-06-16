# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#	- Média abaixo de 5.0: REPROVADO
#	- Média entre 5.0 e 6.9: RECUPERAÇÃO
#	- Média 7.0 ou superior: APROVADO

print()
n1 = float(input("1º nota: "))
n2 = float(input("2º nota: "))
n3 = float(input("3º nota: "))
med = (n1+n2+n3)/3
print()
if (med < 5):
	print(f"Com média {(med):.1f} o aluno está reprovado")
elif (5 <= med < 7):
	print(f"Com média {(med):.1f} o aluno está em recuperação")
else:
	print(f"Com média {(med):.1f} o aluno está aprovado")
print()