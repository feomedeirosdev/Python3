# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
comp = randint(1, 10)

print()
print("Eu sou seu computador!")
print("Acabei de pensar em um número entre 1 e 10 (inclusos)")
print("Você consegue adivinha qual foi?")
play = int(input(">>> "))
print()

cont = 1
while play != comp:
	if (play < comp):
		play = int(input("Tente um número maior: "))
	if (play > comp):
		play = int(input("Tente um número menor: "))
	cont += 1
	
print(f"Você Acertou com {cont+1} tentativas")
print()