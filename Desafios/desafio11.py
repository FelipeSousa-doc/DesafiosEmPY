"""
Crie um programa que converta medidas em metro para
KM,HM,DAM,DM,CM,MM
"""
cores = {'negrito':'\033[1m','fundoazulletraamarla':'\033[31;43m','nenhum':'\033[m'}
print('\033[1;32m=' * 20)
print('     CONVERSOR            ')
print('\033[1;32m='*20)
metro = float(input('\033[mDigite uma distancia em metros: '))

metro_pra_km = (metro /10) / 10 /10
metro_pra_hm = metro / 100
metro_pra_dam = metro / 10
metro_pra_dm = metro * 10
metro_pra_cm = metro * 10 * 10
metro_pra_mm = metro * 10 * 10

print(f'A medida {metro} correposponde a: ')
print(f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_km}{cores['nenhum']}\n'
      f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_hm:.2f}Hm{cores['nenhum']}\n'
      f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_dam}Dam{cores['nenhum']}\n'
      f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_dm}Dm{cores['nenhum']}\n'
      f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_cm}cm{cores['nenhum']}\n'
      f'{cores['negrito']}{cores['fundoazulletraamarla']}{metro_pra_mm}mm{cores['nenhum']}')
