from time import sleep
from emoji import emojize

for c in range(10,0-1,-1):
    print(f'\033[1;32m{c}')
    sleep(1)

print(emojize('\033[1;31mBUUU\033[1;32mUUU\033[1;34mUM!:fireworks:'))
