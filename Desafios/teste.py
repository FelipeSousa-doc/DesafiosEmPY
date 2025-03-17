numero = str(input('Digite um número: '))
novo = 0
s = 0

for c in range(0,len(numero)):
    novo += int(len(numero[c]))
    s += novo

print(f'A soma dos números deu {s}') 
