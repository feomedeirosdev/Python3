# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print()
l0 = int(input("Limite inferior: "))
l = int(input("Limite superior: "))
print()
for i in range(l0, l+1):
	if (i % 3 == 0):
		l0 = i
		break

soma = 0
for i in range(l0, l+1, 3):
	if (i%2==1):
		print(i)
		soma += i

print()
print(soma)