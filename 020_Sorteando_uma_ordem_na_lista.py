# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

print("")
n1 = str(input("1º aluno: "))
n2 = str(input("2º aluno: "))
n3 = str(input("3º aluno: "))
n4 = str(input("4º aluno: "))
print("")
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(alunos)
print("")