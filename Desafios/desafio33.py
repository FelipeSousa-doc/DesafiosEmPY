'''
Crie um programa que leia um número inteiro e mostre 
na tela se ele é PAR ou ÍMPAR.
'''
numero = int(input('Digite um número: '))
print(f'{numero} é Par.' if numero%2 == 0 else f'{numero} é impar.')
