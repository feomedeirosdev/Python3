# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

from unidecode import unidecode

print()
frase = str(input("Digite a frase: ")).strip().upper().split()
frase_concatenada = ''.join(frase)
frase_concatenada = unidecode(frase_concatenada)
frase_invertida = frase_concatenada[::-1]
print()
print(frase_concatenada)
print(frase_invertida)
print()
if(frase_invertida == frase_concatenada):
	print("É palíndromo!")
else:
	print("NÃO é palíndromo!")
print()