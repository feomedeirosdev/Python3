# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# 	- Até 9 anos: MIRIM
# 	- Até 14 anos: INFANTIL
# 	- Até 19 anos: JÚNIOR
# 	- Até 25 anos: SÊNIOR
# 	- Acima de 25 anos: MASTER

from datetime import datetime

print()
ano_atual = datetime.now().year
ano_nasc = int(input("Qual o ano de nascimento do atetla? "))
idade = ano_atual - ano_nasc
print()
if (idade < 9):
	print("mirim".upper())
elif (9 <= idade < 14):
	print("infantil".upper())
elif (14 <= idade < 19):
	print("júnior".upper())
elif (19 <= idade < 25):
	print("sênior".upper())
else:
	print("master".upper())
print()