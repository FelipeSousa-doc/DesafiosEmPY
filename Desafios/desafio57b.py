frase = str(input('Digite algo: ')).upper().strip()
junta = ''.join(frase).replace(' ','')
nova_frase = ''

for x in range(len(junta)-1,-1,-1):
    nova_frase += junta[x]
print(F'{junta} invertido fica {nova_frase}.')
if junta == nova_frase:
        print('É UM POLINDROMO!')
elif junta != nova_frase:
       print('NÃO É UM POLINDROMO!')