# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from unidecode import unidecode # Antes de importar a biblioteca "Unidecode" ela deve ser instalada com o comando "pip install unidecode" no terminal

print()
frase = str(input("Digite uma frase qualquer: ")).strip().upper()
frase2 = unidecode(frase)
print()
print(frase2)
print(frase2.count("A"))
print(frase2.find("A")) # Procura do início ao fim (esquerta pra direita)
print(frase2.rfind("A")) # Procura do fim ao início (direita (R) para esquerda)
print()