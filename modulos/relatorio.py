import os , time 
from verifica import verifica_cpf, verifica_float, verifica_int

def menu_relatorio():

        print()
        print('-ˋˏ✄┈┈┈┈ MÓDULO DE RELATORIO -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ relatorio de suites ')
        print('2 ╰┈➤ relatorio de hospedagens  ')
        print('3 ╰┈➤ relatorio de produtos ')
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

def relatorio_hospedagens(hospedagens):
      resp3 = ''
      while resp3 != 0 :
        os.system('cls')
        os.system('clear')
        print()
        print('-ˋˏ✄┈┈┈┈ RELATORIO HOSPEDAGENS -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ listar todas ')
        print('2 ╰┈➤ listar todas em aberto ou fechadas')
        print('3 ╰┈➤ listar todas em uma faixa de meses')
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
            print('||| NÚMERO |  SUÍTE   |  ENTRADA   |     CPF      |   STATUS   |   SAÍDA    |   VALOR    |||')

            for chave, dados in hospedagens.items():
                  if dados['status'] == 'fechado':
                        print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|{dados['saida'].strftime('%d/%m/%Y'):^12}|{dados['valor_t']:^12.2f}|||")
                  else : 
                        print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|||")
            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 2 :
            opcao = int(input('mostrar todas as hospedagens [ 1 - EM ABERTO | 2 - FECHADO ] \n sua opção : '))
            print('||| NÚMERO |  SUÍTE   |  ENTRADA   |     CPF      |   STATUS   |   SAÍDA    |   VALOR    |||')

            for chave, dados in hospedagens.items():
                  if opcao == 2 :
                        if dados['status'] == 'fechado':
                              print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|{dados['saida'].strftime('%d/%m/%Y'):^12}|{dados['valor_t']:^12.2f}|||")
                  if opcao == 1 : 
                        if dados['status'] != 'fechado':
                              print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|||")
            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 3 :
            achou = False 
            print('informe a faixa de tempo que deseja consultar as hospedagens ')
            faixa_i = int(input('informe o mes inicial : '))
            faixa_f = int(input('informe o mes final : '))
            print('||| NÚMERO |  SUÍTE   |  ENTRADA   |     CPF      |   STATUS   |   SAÍDA    |   VALOR    |||')

            for chave, dados in hospedagens.items():
                  if dados['entrada'].month >= faixa_i and dados['entrada'].month <= faixa_f :

                        achou = True
                        if dados['status'] == 'fechado':
                              print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|{dados['saida'].strftime('%d/%m/%Y'):^12}|{dados['valor_t']:^12.2f}|||")
                        else : 
                              print(f"|||{chave:^8}|{dados['suite']:^10}|{dados['entrada'].strftime('%d/%m/%Y'):^12}|{dados['cpf']:^14}|{dados['status']:^12}|||")
            if not achou :
                  print('nem uma hospedagem foi encontrada nessa faixa de tempo !')     
                  print()             
            print()
            input('Tecle ENTER para continuar...')

def relatorio_produtos(produtos):
      resp3 = ''
      while resp3 != 0 :
        os.system('cls')
        os.system('clear')
        print()
        print('-ˋˏ✄┈┈┈┈ RELATORIO  PRODUTOS -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ listar todos ')
        print('2 ╰┈➤ litar desativados  ')
        print('3 ╰┈➤ listar faixa de preço')
        print('4 ╰┈➤ pesquisar por nome')
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
            print('||| NÚMERO |    PRODUTO    | ESTOQUE |   PREÇO  |||')

            for chave, dados in produtos.items():
                  print(f"|||{chave:^8}|{dados['produto']:^15}|{dados['estoque']:^9}|{dados['valor']:^10}|||")

            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 2 :
            print('||| NÚMERO |    PRODUTO    | ESTOQUE |   PREÇO  |||')
            for chave, dados in produtos.items():
                  if dados['ativo'] == False:
                        print(f"|||{chave:^8}|{dados['produto']:^15}|{dados['estoque']:^9}|{dados['valor']:^10}|||")
            print()
            input('tecle ENTER para continuar.....')
         
        elif resp3 == 3 :
            print('digite a faixa de preço que deseja procurar')
            faixa_i = float(input('proço inicial : '))
            faixa_f = float(input('ate preço final : '))
            print()
            print('||| NÚMERO |    PRODUTO    | ESTOQUE |   PREÇO  |||')
            for chave, dados in produtos.items():
                  if dados['valor'] >= faixa_i and dados['valor'] <= faixa_f:
                        print(f"|||{chave:^8}|{dados['produto']:^15}|{dados['estoque']:^9}|{dados['valor']:^10}|||")
            print()
            input('tecle ENTER para continuar.....')

        elif resp3 == 4 :
            produto = input('digite o nome do produto que procura :')
            achou = False
            print()
            for chave, dados in produtos.items():
                  if dados['produto'] == produto :
                        print('||| NÚMERO |    PRODUTO    | ESTOQUE |   PREÇO  |||')
                        print(f"|||{chave:^8}|{dados['produto']:^15}|{dados['estoque']:^9}|{dados['valor']:^10}|||")
                        achou = True
            if not achou :
                  print('produto não encontrado')
            print()
            input('tecle ENTER para continuar.....')

def relatorio_pedidos(pedidos,produtos):
      resp3 = ''
      while resp3 != 0 :
        os.system('cls')
        os.system('clear')
        print()
        print('-ˋˏ✄┈┈┈┈ RELATORIO  PEDIDOS -ˋˏ✄┈┈┈┈')
        print()
        print('1 ╰┈➤ listar todos ')
        print('2 ╰┈➤ litar desativados  ')
        print('3 ╰┈➤ listar em aberto ou fechados')
        print('4 ╰┈➤ listar faixa de preço')
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
            print('||| NÚMERO | HOSPEDAGEM |    PRODUTO     | QUANTIDADE |   STATUS   |||')

            for chave, dados in pedidos.items():
                  print(f"|||{chave:^8}|{dados['hospedagem']:^12}|{produtos[dados['produto']]['produto']:^16}|{dados['quantidade']:^12}|{dados['status']:^12}|||")

            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 2:
            print('||| NÚMERO | HOSPEDAGEM |    PRODUTO     | QUANTIDADE |   STATUS   |||')

            for chave, dados in pedidos.items():
                  if dados['ativo'] == False:
                        print(f"|||{chave:^8}|{dados['hospedagem']:^12}|{produtos[dados['produto']]['produto']:^16}|{dados['quantidade']:^12}|{dados['status']:^12}|||")

            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 3:
            opcao = int(input('mostrar todos os pedidos [ 1 - EM ABERTO | 2 - FECHADO ] \n sua opção : '))
            print('||| NÚMERO | HOSPEDAGEM |    PRODUTO     | QUANTIDADE |   STATUS   |||')

            for chave, dados in pedidos.items():
                  if opcao == 1 :
                        if dados['status'] ==  'em aberto':
                              print(f"|||{chave:^8}|{dados['hospedagem']:^12}|{produtos[dados['produto']]['produto']:^16}|{dados['quantidade']:^12}|{dados['status']:^12}|||")
                  elif opcao == 2 :
                        if dados['status'] ==  'fechado':
                              print(f"|||{chave:^8}|{dados['hospedagem']:^12}|{produtos[dados['produto']]['produto']:^16}|{dados['quantidade']:^12}|{dados['status']:^12}|||")
            print()
            input('Tecle ENTER para continuar...')

        elif resp3 == 4 :
            print('digite a faixa de preço que deseja procurar')
            faixa_i = float(input('proço inicial : '))
            faixa_f = float(input('ate preço final : '))
            print()
            print('||| NÚMERO | HOSPEDAGEM |    PRODUTO     | QUANTIDADE |   STATUS   |||')
            for chave, dados in pedidos.items():
                  if produtos[dados['produto']]['valor'] >= faixa_i and produtos[dados['produto']]['valor'] <= faixa_f:
                        print(f"|||{chave:^8}|{dados['hospedagem']:^12}|{produtos[dados['produto']]['produto']:^16}|{dados['quantidade']:^12}|{dados['status']:^12}|||")
            print()
            input('tecle ENTER para continuar.....')