'''
Faça um programa que leia o nome completo de 
uma pessoa, mostrando em seguida o primeiro e o 
último nome separadamente. Exemplo: Ana Cláudia Silva
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0].title()))
print('Seu último nome é {}'.format(nome.split()[-1].title()))
