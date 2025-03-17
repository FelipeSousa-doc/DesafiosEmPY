peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

print(f'Seu IMC é {imc:.2f}.')

if imc < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO!')

elif imc < 25:
    print('Você está no \033[32;1mPESO IDEAL. Parabéns!')

elif imc < 30:
    print('Você está no \033[33;1mSOBREPESO.')

elif imc < 40:
    print('Você está com \033[1;31mOBESIDADE.')
    
else:
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA\033[m. \033[1;31mCUIDADO!')
