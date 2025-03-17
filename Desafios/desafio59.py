peso = float(input('Digite o peso da 1ª pessoa: '))

menor_peso = peso
maior_peso = peso
for c in range(2,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if peso < menor_peso :
        menor_peso = peso
    elif  peso > maior_peso:
        maior_peso = peso

print(f'O menor peso foi {menor_peso}.')
print(f'O maior peso foi {maior_peso}.')
