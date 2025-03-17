print('-' * 20)
print('FIBONACCI')
print('-' * 20)

termos = int(input('Quantos termos você quer mostrar? '))
c = 0
z = 0
x = 1
v = 0

print('~' * 50)
while c <= termos - 3:
    if c == 0:
        v = z + x
        print(f'{z} -> {x} -> {v}', end=' -> ')
    else:
        z = x
        x = v
        v = z + x
        print(f'{v}', end=' -> ')
    c += 1  
print('FIM!!')
print('~' * 50)