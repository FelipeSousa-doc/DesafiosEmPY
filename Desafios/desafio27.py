'''
 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
cidade = str(input('Em qual cidade você nasceu? ')).strip()
santo_cap = cidade.title()
print('Santo' in santo_cap[:5])