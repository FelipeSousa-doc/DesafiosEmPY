from datetime import date

ano = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = ano - nasc

print(f'O atleta tem {idade} anos.')

if idade <=9:
    print('O atleta é MIRIM.')

elif 14>= idade >9:
    print('O atleta é INFANTIL.')

elif 14 < idade <=19:
    print('O atleta é JUNIOR.')

elif 25 >= idade:
    print('O atleta é SÊNIOR.')

elif idade > 25:
    print('O atleta é MASTER.')
    