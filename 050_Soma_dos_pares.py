# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print()

num = []

for i in range(1, 7):
	n = int(input(f"Entre com o {i}º número: "))
	num.append(n)

print()
print(num)
soma = 0
for i in num:
	if(i%2==0):
		soma += i
print()	
print(soma)
print()