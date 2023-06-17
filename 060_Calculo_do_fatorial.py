# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print()

num = str(input("Digite o número: "))
while not num.isdigit():
	num = str(input("Digite o número: "))
num = int(num)

fat_f = 1
for i in range(num, 0, -1):
	fat_f *= i
print(fat_f)

fat_w = 1
while num > 1:
	fat_w *= num
	num -= 1
print(fat_w)

print()