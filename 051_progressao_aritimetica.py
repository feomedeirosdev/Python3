# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print()
a1 = int(input("Qual é o 1º termo: "))
r = int(input("Qual é a razão: "))
n = int(input("Quantos termos deseja? "))

an = a1 + (n - 1) * r
sn = (n/2) * (a1 + an)

soma = 0
for i in range(a1, an+1, r):
	print(i, end=' -> ')
	soma += i
print("Fim!")
print()
print(soma)
print(sn)
print()