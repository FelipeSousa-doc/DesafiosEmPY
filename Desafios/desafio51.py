from time import sleep

print('\033[1;36mNúmeros pares entre 1 e 50: ')

for numero in range(1,51):
    if numero >=20 and numero % 2 == 0:
        print(f'\033[1;34m{numero}\033[1m, ',end='')
        sleep(0.5)
    elif numero %2 == 0 and numero<20:
        print(f'\033[1;35m{numero}\033[1m, ',end='')
        sleep(0.5)

print('\033[1;33mFIM!!!')