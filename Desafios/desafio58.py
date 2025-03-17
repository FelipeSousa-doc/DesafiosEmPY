import datetime
ano_atual = datetime.date.today().year
menor_id = 0
maior_id = 0
for c in range(1,8):
    ano_nasc = int(input(F'Ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior_id += 1 
    elif idade < 18:
        menor_id += 1
print(f'{maior_id} pessoas desse grupo são maiores de idade') 
print(f'{menor_id} pessoas são menores de idade.')