'''
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''
from colorama import init, Fore
import time
init()

velocidade_car = float(input('Digite a velocidade do carro: '))
print(Fore.LIGHTYELLOW_EX + 'VRUUUUUUUUUUUUUUUUUUUUUM... PÁ')
time.sleep(1.3)
if velocidade_car>80:
    print(Fore.RED + 'Você foi mutado, excedeu o limite de velocidade que é 80KM, e pagará', Fore.YELLOW + f'R${(velocidade_car - 80) * 7:.2F}')
else:
    print(Fore.GREEN + 'Tudo tranquilo, liberado!')
print(Fore.CYAN + 'Boa viagem!')
