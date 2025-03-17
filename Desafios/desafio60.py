soma_i = 0
idade_m = 0
idade_men_vin = 0
nome_h  = ''

for c in range(1,5):
    nome = str(input(f'Qual o nome da {c}ª pessoa? ')).capitalize().strip()
    idade = int(input(f'Qual a idade da {c}ª pessoa? '))
    sexo = str(input(f'Qual o sexo da {c}ª pessoa? ')).capitalize().strip()
    soma_i += idade
    print('-' * 20)
    if c == 1:
        idade_h = idade
        nome_h = nome
    elif sexo == 'M' and idade > idade_h:
        idade_h = idade
        nome_h = nome
    elif sexo == 'F' and idade < 20:
        idade_men_vin += 1

media = soma_i / 4

print(f'''A media de idade do grupo foi \033[1m{media}\033[m.
O homem mais velho é o {nome_h}, com \033[1m{idade_h}\033[m anos.
Mulheres menores de 20 anos \033[1m{idade_men_vin}\033[m.
''')
