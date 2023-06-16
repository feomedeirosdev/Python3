# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print()
print("Vamos jogar Pedra, Papel e Tesoura")
print("Faça sua escolha:")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
player = int(input("> "))
comp = randint(1,3)
print()
sleep(.5)
print("JO")
sleep(.5)
print("KEN")
sleep(.5)
print("PO!")
sleep(.5)
print()
if (player == comp):
	if (player == 1):
		print("Jogador: Pedra")
		print("Computador: Pedra")
		print("EMPATE")
	elif (player == 2):
		print("Jogador: Papel")
		print("Computador: Papel")
		print("EMPATE")
	elif (player == 3):
		print("Jogador: Tesoura")
		print("Computador: Tesoura")
		print("EMPATE")
elif (player == 1): # Jogador Pedra
	if (comp == 2):
		print("Jogador: Pedra")
		print("Computador: Papel")
		print("Computador Vence!")
	elif (comp == 3):
		print("Jogador: Pedra")
		print("Computador: Tesoura")
		print("Jogador Vence!")
elif (player == 2): # Jogador Papel
	if (comp == 1):
		print("Jogador: Papel")
		print("Computador: Pedra")
		print("Jogador Vence!")
	elif (comp == 3):
		print("Jogador: Papel")
		print("Computador: Tesoura")
		print("Computador Vence!")
elif (player == 3): # Jogador Tesoura
	if (comp == 1):
		print("Jogador: Tesoura")
		print("Computador: Pedra")
		print("Computador Vence!")
	elif (comp == 2):
		print("Jogador: Tesoura")
		print("Computador: Papel")
		print("Jogador Vence!")
else:
	print("Jogada Inválida!")
print()