primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
form = primeiro_termo + (10 - 1) * razao
c = primeiro_termo

while c <=form:
    print(f'{c} -> ',end='')
    c += razao

print('FIM!!')