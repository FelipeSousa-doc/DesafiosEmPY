"""
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
Dólares ela pode comprar.
Considere US$1.00 = R$3.27
"""
dinheiro = float(input('Quanto de dinheiro você tem? R$'))
dolares = dinheiro/3.27

print(f'Você pode comprar US$\033[1;32m{dolares:.2f}')
