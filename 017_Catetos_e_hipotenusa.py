# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

print("")
c1 = float(input("Entre com o valor do 1º cateto em cm: "))
c2 = float(input("Entre com o valor do 2º cateto em cm: "))
print("")
print(f"O valor da hipotenusa é: {(c1**2 + c2**2)**(1/2)} cm")
print(f"O valor da hipotenusa é: {pow((c1**2 + c2**2),(1/2))} cm")
print(f"O valor da hipotenusa é: {math.hypot(c1, c2)} cm")
print("")