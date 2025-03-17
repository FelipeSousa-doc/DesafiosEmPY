'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random
aluno_1 = input('Digite o primeiro aluno: ')
aluno_2 = input('Digite o segundo aluno: ')
aluno_3 = input('Digite o terceiro aluno: ')
aluno_4 = input('Digite o quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print(f'O aluno escolhido foi {random.choice(lista)}')
