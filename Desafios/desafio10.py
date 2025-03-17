"""
Desenvolva um programa que leia quatro notas
de um aluno e calcule a média.
"""
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média das notas \033[1m{nota_1}, {nota_2}, {nota_3}\033[m e \033[1m{nota_4} é \033[4m{media:.2f}')
