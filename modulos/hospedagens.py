from verifica import verifica_cpf, verifica_int , verifica_float
from datetime import datetime

def menu_hospedagens():
    print()
    print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
    print()
    print('1 ࣪ ִֶָ☾.   Fazer check-in     ࣪ ִֶָ☾.')
    print('2 ࣪ ִֶָ☾. consultar hospedagem ࣪ ִֶָ☾.')
    print('3 ࣪ ִֶָ☾.   Fazer check-out    ࣪ ִֶָ☾.')
    print('0 ࣪ ִֶָ☾.       voltar         ࣪ ִֶָ☾.')
    print()
    resp2 = input('🤍ྀི  digite o numero da operação : ')
    while not verifica_int(resp2):
            print()
            print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
            print()
            resp2 = input('🤍ྀི  digite o numero da operação : ')
    resp2 = int(resp2)
    return resp2

def cadastrar_hospedagens(hospedagens,suites):
          livre = 0
          for chave, dados in suites.items():
            if dados['status'] == 'livre' and dados['ativo'] :
              livre += 1
          if livre > 0 :
              print()
              print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-IN ✩₊˚.⋆☾⋆⁺₊✧')
              print()
              print('SUITES LIVRES:')
              print()
              for chave, dados in suites.items():
                if dados['status'] == 'livre' and dados['ativo']:
                  print(f'|||   SUITE NÚMERO  > {chave:^5} |   TTPO   >  {dados['tipo']:^10} |   VALOR POR HR   >   R${dados['valor']:^10} |||')
                  print()
              print()
              num = len(hospedagens)+1
              print(f'NUMERO DA SUA HOSPEDAGEM -> {num}')
              print()
              suite = input('ָ☾. digite o numero da suite que deseja : ')
              while not verifica_int(suite):
                print()
                print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                print()
                suite = input('🤍ྀི  digite o numero da suite que deseja : ')
              suite = int(suite)

              while suite not in suites or (suites[suite]['status'] != "livre" and suites[suite]['ativo'] == False) :
                  print('suíte invalida, digite uma suíte disponivel.')
                  suite = input('ָ☾. digite o numero da suite que deseja : ')
                  while not verifica_int(suite):
                    print()
                    print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                    print()
                    suite = input('🤍ྀི  digite o numero da suite que deseja : ')
                  suite = int(suite)
              cpf = input('ָ☾. digite o seu CPF : ')
              while verifica_cpf(cpf) == False :
                print('      ! CPF INVALIDA !')
                cpf = input('ָ☾. digite o seu CPF : ')

              entrada = datetime.now()
              print()
              hospedagens[num] = {
              'suite' : suite,
              'entrada' : entrada,
              'cpf' : cpf,
              'status' : 'em aberto',
              }
              suites[suite]['status'] = 'ocupado'
              print('check-in feita com suscesso ! ')
              input('tecle ENTER pra contimuar....')
          else :
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-IN ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            print('!! todas as suites estão cheias  !! ')
            print()
            input('tecle ENTER pra contimuar....')

def consultar_hospedagens():
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ CONSULTAR HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          print('1 ָ☾. listar todas')
          print('2 ָ☾. buscar por numero')
          print()
          resp3 = input('🤍ྀི  digite o numero da operação : ')
          while not verifica_int(resp3):
            print()
            print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
            print()
            resp3 = input('🤍ྀི  digite o numero da operação : ')
          resp3 = int(resp3)
          return resp3

def listagem_hospedagens(hospedagens):
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ LISTAGEM DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            for chave, dados in hospedagens.items():
              print()
              print('☪-☪'*65)
              print()
              print(f'||| HOSPEDAGEM NÚMERO  > {chave:^5} |   SUITE   >  {dados['suite']:^10} |  ENTRADA   >  {dados['entrada']} | CPF  >   {dados['cpf']:^10} | | STATUS   >   {dados['status']:^10} |')
              if dados['status'] == 'fechado' :
                print(f'|   SAIDA   >  {dados['saida']} |  VALOR TOTAL   >   R${dados['valor_t']:.2f} |||')
                print()
            print()
            print('☪-☪'*65)
            print()
            input('tecle ENTER para continuar ....')

def pesquisa_hospedagens(hospedagens):
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE HOSPEDAGENS ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            num = input('digite o numero da hospedagem que deseja consultar : ')
            while not verifica_int(num):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              num = input('🤍ྀི  digite o numero da hospedagem que deseja consultar : ')
            num = int(num)
            if num in hospedagens :
              print()
              print('☪-☪'*60)
              print()
              print(f'||| HOSPEDAGEM NÚMERO  > {num:^5} |   SUITE   >  {hospedagens[num]['suite']:^10} |  ENTRADA   >  {hospedagens[num]['entrada']} | CPF  >   {hospedagens[num]['cpf']:^10} | | STATUS   >   {hospedagens[num]['status']:^10} |')
              if hospedagens[num]['status'] == 'fechado' :
                print(f'|   SAIDA   >  {hospedagens[num]['saida']} |  VALOR TOTAL   >   R${hospedagens[num]['valor_t']:.2f} |||')
              print()
              print('☪-☪'*60)
              print()
              input('tecle ENTER para continuar ....')
            else :
              print(f'hospedagem numero {num} não encontrada')
              input('pres ENTER para continuar....')

def finalizar_hospedagens(hospedagens,suites,pedidos,produtos):
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-OUT ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = input('digite o numero da hospedagem : ')
          while not verifica_int(num):
            print()
            print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
            print()
            num = input('🤍ྀི  digite o numero da hospedagem : ')
          num = int(num)
          if num in hospedagens:
            saida = datetime.now()
            print()
            hospedagens[num]['saida'] = saida
            print()
            print(f'☾. numero -> {num}')
            print(f'ָ☾. suíte -> {hospedagens[num]['suite']}')
            print(f'ָ☾. entrada -> {hospedagens[num]['entrada']}')
            print(f'ָ☾. CPF -> {hospedagens[num]['cpf']}')
            print(f'ָ☾. status -> {hospedagens[num]['status']}')
            print(f'ָ☾. saida -> {hospedagens[num]['saida']}')
            tempo_t = hospedagens[num]['saida'] - hospedagens[num]['entrada']
            tempo_t = tempo_t.total_seconds() / 3600
            valor_hospedagem = tempo_t * suites[hospedagens[num]['suite']]['valor']
            print(f'ָ☾. valor da hospedagem -> R${valor_hospedagem:.2f}')

            valor_consumo = 0
            for i in range(1,len(pedidos)+1) :
              if pedidos[i]['hospedagem'] == num :
                 valor_consumo += produtos[pedidos[i]['produto']]['valor'] * pedidos[i]['quantidade']

            valor_t = valor_consumo + valor_hospedagem
            print(f'ָ☾. valor de consumo -> R${valor_consumo}')  
            print(f'ָ☾. valor total -> R${valor_t:.2f} ')
            print()
            suite = hospedagens[num]['suite']
            resp4 = input('dejeja fechar essa hospedagem ? [S/N] ')
            if resp4 in 'Ss' :
              suites[suite]['status'] = 'livre'
              hospedagens[num]['status'] = 'fechado'
              hospedagens[num]['valor_t'] = valor_t
              for i in range(1,len(pedidos)+1) :
                if pedidos[i]['hospedagem'] == num and pedidos[i]['ativo']:
                  pedidos[i]['status'] = 'fechado'

              print('check-out realizado com suscesso !')
            else :
              print('check-out cancelado')
              del(hospedagens[num]['saida'])
          else:
            print(f'hospedagem numero {num} não encontrada')
            input('pres ENTER para continuar....')
          input('press ENTER para continuar....')

