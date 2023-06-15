# Ex016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
print("")
n = float(input("Digite um número real: "))
print("")
print(f"P valor digitado foi {n} e sua porção inteira é: {math.trunc(n)}")
print("")