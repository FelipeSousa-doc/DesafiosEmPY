sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

while sexo != 'F' and sexo != 'M':    
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo: [M/F]: ')).strip().upper()

if sexo == 'M':
    print(f'Sexo Masculino registrado!')
else:
    print(f'Sexo Feminino registrado!')