'''
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import sample

aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
lista_random = sample(lista, k=(len(lista)) )
print(f'A lista de apresentação será: {lista_random}')
