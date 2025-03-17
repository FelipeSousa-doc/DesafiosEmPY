'''
calcular a área de um círculo? 
O usuário informa o raio, 
e o programa calcula e exibe o resultado.
'''

try:
    raio = int(input('Digite um número inteiro: '))
    if raio < 0:
        print('O raio não pode ser negativo')
    else:
        area = 3.14 * raio ** 2
        print(f'A área do circulo com raio de {raio} é {area}')
except:
    print('Insira um número inteiro valido! ')