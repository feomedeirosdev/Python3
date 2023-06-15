# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

print("")
ang = float(input("Entre com o valor do angulo em graus: "))
rad = math.radians(ang)
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print("")
print(f"{ang}º em radianos é: {rad} rad")
print(f"Seno: {sin}")
print(f"Cosseno: {cos}")
print(f"Tangente: {tan}")
print("")