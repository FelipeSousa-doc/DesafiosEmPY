'''
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
aluno_1 = str(input('Aluno 1: '))
aluno_2 = str(input('Aluno 2: '))
aluno_3 = str(input('Aluno 3: '))
aluno_4 = str(input('Aluno 4: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista)

print('A ordem de apresentação vai ser {}'.format(lista))
