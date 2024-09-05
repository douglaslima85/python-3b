print('Camisetas\n')

print('1. Cadastro de camisetas')
print('2. Lista de camisetas')
print('3. Ativar camisetas')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: ') )
print('Você escolheu a opção: ' , opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar camisetas')
elif opcao_escolhida == 2:
    print('Lista de camisetas')
elif opcao_escolhida == 3:
    print('Ativar/desativar camisetas')
else:
    print('Saindo da aplicação')