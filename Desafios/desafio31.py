'''
Escreva um pograma que faça o computador
"pensar" em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador. O programa 
deverá escrever na tela se o usuário venceu ou perdeu.
'''

from colorama import init, Fore
import time
from random import randint
init()

numero_pensado = randint(0,5)

print(Fore.CYAN + '-_' * 25)
print(Fore.LIGHTGREEN_EX + 'Pensarei em um número de 0 a 5, tente me vencer!')
print(Fore.CYAN + '-_' * 25)
numero = int(input(Fore.WHITE + 'Qual número eu estou pensando? '))

print(Fore.BLUE + 'PROCESSANDO...')
time.sleep(1.4)
if numero == numero_pensado:
    print(Fore.GREEN + 'VOCÊ ACERTOU!! o número pensado por mim foi {}'.format(numero_pensado))
else:
    print(Fore.RED + 'Você errou! eu pensei no número {}'.format(numero_pensado))
