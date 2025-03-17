'''
 Faça um programa que leia três números 
 e mostre qual é o maior e qual é o menor.
'''
from colorama import init, Fore

init()

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 > n2 and n1 > n3:
    maior = n1

if n2 > n3 and n2 > n1:
    maior = n2

elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1

if n2<n1 and n2<n3:
    menor = n2

elif n3 < n1 and n3 < n2:
    menor = n3

print('O maior foi ', Fore.YELLOW + F'{maior}',Fore.WHITE +'.')
print(Fore.WHITE + 'O menor foi ',Fore.BLUE + F'{menor}',Fore.WHITE +'.')
