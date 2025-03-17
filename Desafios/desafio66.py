primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

c = 1
f = 10
resp = 1
pul = primeiro_termo
cont_t = 0
form = 0

while c <= f and resp != 0:
    print(f'{pul} -> ',end='')
    pul += razao 
    c+= 1 
    cont_t += 1 

    if c>f:
        while resp!=0:
            print('Pausa!')
            resp = int(input('Quantos termos a mais quer mostrar?: '))
            c = 1
            cont_t += resp
            while c<= resp:
                pul += razao
                print(f'{pul} ->',end=' ')
                c+=1

print('FIM!')
print(f'Foram mostrados {cont_t} termos')
