from random import randint
from time import sleep
print('''Acabei de pensar em um número entre 0 e 10.
Qual número eu estou pensando?
''',end='')

pensado = randint(0,10)
palpite = int(input('Qual você acha que foi? '))
tentativas = 1

while palpite != pensado:
    tentativas += 1 
    if pensado > palpite:
        print('É maior. tente de novo!')
        palpite = int(input('Qual seu palpite? '))
    elif pensado < palpite:
        print('É menor... Tente de novo.')
        palpite = int(input('Qual seu palpite? '))

print('Processando...')
sleep(1)
print(f'Parabéns. Você acertou com {tentativas} tentativas.')