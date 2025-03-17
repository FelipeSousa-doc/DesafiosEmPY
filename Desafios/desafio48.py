print('='*30)
print('LOJÃO VENDE BARATO')
print('='*30)

preco = float(input('Qual o valor da compra? R$'))

print('FORMA DE PAGAMENTO:'
      '\n[1] à vista dinheiro/pix.'
      '\n[2] à vista cartão.'
      '\n[3] 2x no cartão.'
      '\n[4] 3x ou mais no cartão.')

preco_c_d = 0

opcao = int(input('Escolha: '))

if opcao == 1:
    preco_c_d = preco - (preco * 10 / 100)
    print(f'Você pagará R${preco_c_d:.2f} na sua compra de R${preco:.2f}.')

elif opcao == 2:
    preco_c_d = preco - (preco * 5 / 100)
    print(F'Você pagará R${preco_c_d:.2f} na sua compra de R${preco:.2f}.')

elif opcao == 3:
    print(f'Você pagará 2x de R${preco/2:.2f}, total de R${preco:.2f}.')

elif opcao == 4:
    preco_c_d = preco + (preco*20/100)
    opcao2 = int(input('Quantas parcelas será? '))
    print(f'Sua compra será parcelada em {opcao2}x de R${preco_c_d / opcao2:.2f} COM JUROS.\n'
          f'Irá sair R${preco_c_d:.2f} no final. Uma compra que era R${preco:.2f}.')
    
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
    