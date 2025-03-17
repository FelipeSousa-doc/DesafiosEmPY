frase = str(input('Digite uma frase: ')).upper()
frasejun = ''.join(frase).replace(' ','')
invert = frasejun[::-1]
print(F'O inverso de {frasejun} é {invert}')
if frasejun == invert:
    print('É um PÁLINDROMO!')
elif frasejun != invert:
    print('Não é um PALÍNDROMO!')
