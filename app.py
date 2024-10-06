import os

camiseta = [{'nome':'Kamila', 'categoria':'adulto', 'ativo':True},
             {'nome':'Anilda', 'categoria':'adolescente','ativo':True},
             {'nome':'Osmar', 'categoria':'fiminina','ativo':False},
             {'nome':'Ana', 'categoria':'infantil', 'ativo':True}]

def exbir_subtitulo(texto):
    os.system('cle')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():
 print(''''
      
  𝒄𝒂𝒎𝒊𝒔𝒆𝒕𝒂𝒔 
      
 ''')

def mostra_escolhas():
    print('1. Cadastro de camiseta')
    print('2. Listar camiseta')
    print('3. Ativar camiseta')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_camiseta()
        elif opcao_escolhida == 2:
            mostrar_camiseta()
        elif opcao_escolhida == 3:
              alterar_estado_camiseta()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def mostrar_camiseta():
    exbir_subtitulo('Listar camiseta')

    for camiseta in camiseta:
        nome_camiseta = camiseta['nome']
        categoria = camiseta['categoria']
        ativo = camiseta['ativo']
        print(f' - {nome_camiseta} | {categoria} | {ativo}')
    
    retorna_menu_principal()

def alterar_estado_camiseta():
    exbir_subtitulo('Cadastrar camiseta')
    nome_camiseta = input('Qual camiseta(a) você gostaria de mudar o status?')
    camiseta_encontrado = False

    for camiseta in camiseta:
        if nome_camiseta == camiseta['nome']
            camiseta_encontrado = True
            camiseta['ativo'] = not camiseta['ativo']
            mensagem = f'O {nome_camiseta} foi ativado com sucesso' if camiseta['ativo'] else f' O(A) {nome_camiseta} foi desativado'

            print(mensagem)
    if not camiseta_encontrado:
        print('O camiseta ou camiseta não existe')

def finalizar_programa():
    os.system('cle')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()