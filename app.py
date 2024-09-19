import os

def mostra_titulo():
 print(''''
      
  𝒄𝒂𝒎𝒊𝒔𝒆𝒕𝒂𝒔 
      
 ''')

def mostra_escolhas():
  print('1. Cadastro de camisetas')
  print('2. Lista de camisetas')
  print('3. Ativar camisetas')
  print('4. Sair da aplicação')



def escolhe_opcao():
     try:
      opcao_escolhida = int(input('Escolha uma opção: ') )
     print('Você escolheu a opção: ' , opcao_escolhida)

     def finalizar_programa():
      os.system('cle')
     print('Finalizando programa')
 def opcao_invalida():
  print('Esse caracter não é permitido')
input('Digite qualquer tecla')
main()


if opcao_escolhida == 1:
    print('Cadastrar camisetas')
elif opcao_escolhida == 2:
    print('Lista de camisetas')
elif opcao_escolhida == 3:
    print('Ativar/desativar camisetas')
elif opcao_escolhida == 4:
   finalizar_progama()
else:
    opcao_invalida() 
    
def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()
    
if __name__ == '__main__':
    main()