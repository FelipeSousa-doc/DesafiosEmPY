menor_peso = 0
maior_peso = 0

for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'A pessoa mais pesada tem {maior_peso}KG\n'
      f'A mais leve tem {menor_peso} KG.')
