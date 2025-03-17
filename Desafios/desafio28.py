'''
 Crie um programa que leia o nome de uma pessoa 
 e diga se ela tem "SILVA" no nome.
'''
nome = str(input('Digite seu nome: ')).strip()
nome_t = nome.title()
print('Seu nome tem Silva? {}'.format('Silva' in nome_t))
