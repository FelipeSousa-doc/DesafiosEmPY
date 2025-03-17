'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
distancia = float(input('Qual a distância da viagem?(KM): '))
if distancia<=200:
    print(F'A passagem vai custar R${0.50*distancia}')
else:
    print(F'A passagem vai custar R${0.45*distancia}')