# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

print("")
n1 = str(input("1º aluno: "))
n2 = str(input("2º aluno: "))
n3 = str(input("3º aluno: "))
n4 = str(input("4º aluno: "))
print("")
alunos = [n1, n2, n3, n4]
escolhido = random.choice(alunos)
print(f"O aluno escolhido foi {escolhido}")
print("")
num = random.randint(0,4)
print(num)
print(f"O aluno escolhido foi {alunos[num]}")
print("")