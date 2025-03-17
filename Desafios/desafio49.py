from random import choice
import time
import emoji

print(emoji.emojize('''Você pode jogar:
[ 0 ] PEDRA ✊
[ 1 ] PAPEL 🤚
[ 2 ] TESOURA :victory_hand:
'''))

computador = ['Pedra','Papel','Tesoura']
jogada = int(input('Qual sua escolha? '))
jogada_pc = choice(computador)

print('\033[1;33mJO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!\033[m')
print('='*40)

if jogada == 0 and jogada_pc == 'Papel':
    print('Jogador jogou Pedra')
    print('Computador jogou papel')
    print('=' * 40)
    print('COMPUTADOR VENCE')

elif jogada == 0 and jogada_pc == 'Tesoura':
    print('Jogador jogou Pedra')
    print('Computador jogou Tesoura')
    print('=' * 40)
    print('JOGADOR VENCE')

elif jogada == 1 and jogada_pc == 'Pedra':
    print('Jogador jogou Papel')
    print('Computador jogou Pedra')
    print('=' * 40)
    print('JOGADOR VENCE!')

elif jogada == 1 and jogada_pc == 'Tesoura':
    print('Jogador jogou Papel')
    print('Computador jogou Tesoura')
    print('=' * 40)
    print('COMPUTADOR VENCE!')

elif jogada == 2 and jogada_pc == 'Papel':
    print('Jogador jogou Tesoura')
    print('Computador jogou Papel')
    print('=' * 40)
    print('JOGADOR VENCE')

elif jogada == 2 and jogada_pc == 'Pedra':
    print('Jogador jogou Tesoura')
    print('Computador jogou Pedra')
    print('=' * 40)
    print('COMPUTADOR VENCE!')
    
else:
    print('Empate! As jogadas foram iguais')
