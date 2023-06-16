# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print()
num = int(input("Qual número deseja saber a tabuada: "))
print()
for i in range(0, 11):
	print(f"{num} X {i:2} = {num*i}")
print()