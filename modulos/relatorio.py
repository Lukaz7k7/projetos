import os , time 
from verifica import verifica_cpf, verifica_float, verifica_int

def menu_relatorio():

        print()
        print('-ˋˏ✄┈┈┈┈ MÓDULO DE RELATORIO -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ relatorio de suites ')
        print('2 ╰┈➤ relatorio de hospedagens  ')
        print('3 ╰┈➤ relatorio de consumo ')
        print('4 ╰┈➤ relatorio de pedidos ')
        print('0 ╰┈➤ voltar ')
        print()
        resp2 = input('🤍ྀི digite o numero da operação : ')
        while not verifica_int(resp2):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              resp2 = input('🤍ྀི  digite o numero da operação : ')
        resp2 = int(resp2)
        return resp2

def relatorio_suites(suites):
      resp3 = ''
      while resp3 != 0 :
        os.system('cls')
        os.system('clear')
        print()
        print('-ˋˏ✄┈┈┈┈ RELATORIO SUÍTES -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ listar todas ')
        print('2 ╰┈➤ litar desativadas  ')
        print('3 ╰┈➤ listar livres ou ocupadas')
        print('0 ╰┈➤ voltar ')
        print()
        resp3 = input('🤍ྀི digite o numero da operação : ')
        print()
        while not verifica_int(resp3):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              resp3 = input('🤍ྀི  digite o numero da operação : ')
        resp3 = int(resp3)
        os.system('cls')
        os.system('clear')

        if resp3 == 1:
            print('||| NÚMERO |   TIPO   |  PREÇO   |  STATUS  |||')
            for chave, dados in suites.items():
                  print(f"|||{chave:^8}|{dados['tipo']:^10}|{dados['valor']:^10}|{dados['status']:^10}|||")
            print()
            input('tecle ENTER para continuar.....')

        elif resp3 == 2 :
            print('||| NÚMERO |   TIPO   |  PREÇO   |  STATUS  |||')
            for chave, dados in suites.items():
                  if dados['ativo'] == False:
                        print(f"|||{chave:^8}|{dados['tipo']:^10}|{dados['valor']:^10}|{dados['status']:^10}|||")
            print()
            input('tecle ENTER para continuar.....')
         
        elif resp3 == 3 :
            opcao = int(input('deseja ver as suites [ 1 - OCUPADAS | 2 - LIVRES ] : '))
            print()
            if opcao == 1 :
                  opcao = 'ocupado'
            elif opcao == 2:
                  opcao = 'livre'
            else :
                  print('resposta invalida')
            print()
            print('||| NÚMERO |   TIPO   |  PREÇO   |  STATUS  |||')
            for chave, dados in suites.items():
                  if dados['status'] == opcao:
                        print(f"|||{chave:^8}|{dados['tipo']:^10}|{dados['valor']:^10}|{dados['status']:^10}|||")
            print()
            input('tecle ENTER para continuar.....')



def relatorio_produtos()

