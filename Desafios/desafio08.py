"""
 Faça um programa que leia um número Inteiro
 e mostre na tela o seu sucessor e seu antecessor.
"""
numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'Analisando o valor \033[1;31m{numero}\033[m, o antecessor é \033[1;33m{antecessor}\033[m e o sucessor é \033[1;33m{sucessor}')
