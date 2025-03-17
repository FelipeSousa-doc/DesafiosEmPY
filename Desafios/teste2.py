vogais = {'a','e','i','o','u'}

frase = str(input('Digite algo: '))
frase_m = ''.join(frase).lower()
contador_conss = 0
contador_vogal = 0

for c in range(0,len(frase_m)):
    if frase_m[c] in vogais:
        contador_vogal += 1
    elif frase_m[c] not in vogais:
        contador_conss += 1

print(f'Na frase existem {contador_vogal} vogais \nE {contador_conss} conssoantes.')
