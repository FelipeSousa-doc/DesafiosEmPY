termo_1 = int(input('Primeiro termo: '))
razon = int(input('Digite a razão: '))
decimo = termo_1 + (10 - 1) * razon

for c in range(termo_1,decimo + 1, razon):
    print(f'{c} -> ', end ='')
print('FIM!')
