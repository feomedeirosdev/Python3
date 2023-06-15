# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print("")
num = int(input("Digite um número entre 0 e 9999: "))
m = num // 1000
c = (num // 100) % 10
d = (num // 10) % 10
u = (num // 1) % 10
print(m)
print(c)
print(d)
print(u)
print("")

