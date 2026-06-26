import os , time 
from datetime import datetime
from verifica import verifica_cpf, verifica_int, verifica_float
from dados import recupera_suites , salva_suites , recupera_hospedagens, salva_hospedagens, recupera_produtos , salva_produtos, recupera_pedidos, salva_pedidos
from modulos.suites import listagem_suites, cadastrar_suites , menu_suites, pesquisa_suites, consulta_suites , edição_suites , exclui_suites
from modulos.hospedagens import menu_hospedagens

    # recuperando dados dos arquivos

suites = recupera_suites()

hospedagens = recupera_hospedagens()

produtos = recupera_produtos()

pedidos = recupera_pedidos()

resp = ''
while resp != 0 :
    os.system('cls')
    os.system('clear')

    print(''' 
  જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡
𓆩❤︎ 𓆪    ████ █████ █   █     ████ █   █  ████ █████ █████ █   █   𓆩❤︎ 𓆪  
𓆩❤︎ 𓆪   █     █      █ █     █      █ █  █       █   █     ██ ██   𓆩❤︎ 𓆪
𓆩❤︎ 𓆪    ███  ████    █       ███    █    ███    █   ████  █ █ █   𓆩❤︎ 𓆪
𓆩❤︎ 𓆪       █ █      █ █         █   █       █   █   █     █   █   𓆩❤︎ 𓆪
𓆩❤︎ 𓆪   ████  █████ █   █    ████    █   ████    █   █████ █   █   𓆩❤︎ 𓆪
  જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡જ⁀➴ ♡
                     ''')
    
    print('1 ❥ módulo suítes ')
    print('2 ❥ módulo hospedagens')
    print('3 ❥ módolo produtos ')
    print('4 ❥ módolo pedidos ')
    print('5 ❥ módolo de relatorio ')
    print('6 ❥ módolo de informações')
    print('0 ❥ sair ')
    print()
    resp = input('🤍ྀི   digite sua resposta : ')
    while not verifica_int(resp):
      print()
      print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
      print()
      resp = input('🤍ྀི   digite sua resposta : ')
    resp = int(resp)
    os.system('cls')
    os.system('clear')

    # modulo de suítes

    if resp == 1 :
      resp2 = ''
      while resp2 != 0 :
        os.system('cls')
        os.system('clear')

        resp2 = menu_suites()

        os.system('cls')
        os.system('clear')

        if resp2 == 1 :

          cadastrar_suites(suites)

        elif resp2 == 2 :
          
          resp3 = consulta_suites()

          if resp3 == 1 :

            listagem_suites(suites)
            
          else : 
          
            pesquisa_suites(suites)

        elif resp2 == 3  :

          edição_suites(suites)
                
        elif resp2 == 4 :

          exclui_suites(suites)

    # módulo de hospedagem        

    elif resp == 2 :
      resp2 = ''
      while resp2 != 0:
        os.system('cls')
        os.system('clear')

        resp2 = menu_hospedagens()

        os.system('cls')
        os.system('clear')

        if resp2 == 1 :
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

        elif resp2 == 2 :
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
          if resp3 == 1 :
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ LISTAGEM DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            for chave, dados in hospedagens.items():
              print()
              print('☪-☪'*25)
              print()
              print(f'hospedagem numero -> {chave}')
              print()
              print(f'SUITE -> {dados['suite']}')
              print(f'ENTRADA -> {dados['entrada']}')
              print(f'CPF -> {dados['cpf']}')
              print(f'STATUS -> {dados['status']}')
              if dados['status'] == 'fechado' :
                print(f'SAÍDA -> {dados['saida']}')
                print(f'VALOR TOTAL -> R${dados['valor_t']:.2f}')
            print()
            print('☪-☪'*25)
            print()
            input('tecle ENTER para continuar ....')
          else : 
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE HOSPEDAGENS ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            num = input('digite o numero da hospedagem que deseja consultar : ')
            while not verifica_int(resp3):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              num = input('🤍ྀི  digite o numero da hospedagem que deseja consultar : ')
            num = int(num)
            if num in hospedagens :
              print()
              print('☪-☪'*25)
              print()
              print(f'hospedagem numero -> {num}')
              print()
              print(f'SUITE -> {hospedagens[num]['suite']}')
              print(f'ENTRADA -> {hospedagens[num]['entrada']}')
              print(f'CPF -> {hospedagens[num]['cpf']}')
              print(f'STATUS -> {hospedagens[num]['status']}')
              if hospedagens[num]['status'] == 'fechado' :
                print(f'SAÍDA -> {hospedagens[num]['saida']}')
                print(f'VALOR TOTAL -> R${hospedagens[num]['valor_t']:.2f}')
              print()
              print('☪-☪'*25)
              print()
              input('tecle ENTER para continuar ....')
            else :
              print(f'hospedagem numero {num} não encontrada')
              input('pres ENTER para continuar....')
      
        elif resp2 == 3 :
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

    # módulo de produtos         
                    
    elif resp == 3 : 
      resp2 = ''
      while resp2 != 0 :
        os.system('cls')
        os.system('clear')
        print()
        print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅ MÓDULO DE PRODUTOS  ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
        print()
        print('1 𓊯   cadastrar produstos   𓊯')
        print('2 𓊯      ver produtos       𓊯')
        print('3 𓊯     editar produto      𓊯')
        print('4 𓊯     excluir produto     𓊯')
        print('0 𓊯         voltar          𓊯')
        print()
        resp2 = input('🤍ྀི  digite o numero da operação : ')
        while not verifica_int(resp2):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              resp2 = input('🤍ྀི  digite o numero da operação : ')
        resp2 = int(resp2)
        os.system('cls')
        os.system('clear')
        if resp2 == 1 :
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
          print()
          num = max(produtos.keys()) + 1
          print(f'NUMERO DO PRODUTO -> {num}')
          print()
          produto = input('𓊯 digite o nome do produto para cadastrar : ')
          estoque = input('𓊯 digite a quantidade que tem no estoque : ')
          while not verifica_int(estoque):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              estoque = input('🤍ྀི  digite a quantidade que tem no estoque : ')
          estoque = int(estoque)
          valor = input('𓊯 digite o preço do produto : ')
          while not verifica_float(valor):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              valor = input('🤍ྀི  digite o preço do produto : ')
          valor = float(valor)
          produtos[num] = {
        'produto' : produto, 
        'estoque' : estoque,
        'valor' : valor,
        'ativo' : True
        }
          print('produto cadastrado com sucesso')
          input('tecle o ENTER para continuar.....')

        elif resp2 == 2 :
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
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
          if resp3 == 1 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            for chave, dados in produtos.items() :
              if dados['ativo']:
                print()
                print('☕︎ 𓎩 ‧₊˚'*15)
                print()
                print(f'produto numero -> {chave}')
                print()
                print(f'𓊯 nome -> {dados['produto']}')
                print(f'𓊯 estoque -> {dados['estoque']}')
                print(f'𓊯 preço -> R$ {dados['valor']}')
            print()
            print('☕︎ 𓎩 ‧₊˚'*15)
            print()
            input('tecle ENTER para continuar.....')
          
          else :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = input('digite o numero do produto que deseja consultar : ')
            while not verifica_int(num):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              num = input('🤍ྀི  digite o numero do produto que deseja consultar : ')
            num = int(num)
            if num in produtos and produtos[num]['ativo'] :
              print()
              print(f'produto numero -> {num}')
              print()
              print(f'𓊯 nome -> {produtos[num]['produto']}')
              print(f'𓊯 estoque -> {produtos[num]['estoque']}')
              print(f'𓊯 preço -> R$ {produtos[num]['valor']}')
              print()
              input('tecle ENTER para continuar.....')
            else : 
              print(f'produto numero {num} não encontrado')
              input('tecle ENTER para continuar.....')

        elif resp2 == 3 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  EDIÇÃO DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = input('digite o numero do produto que deseja editar : ')
            while not verifica_int(num):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              num = input('🤍ྀི  digite o numero do produto que deseja consultar : ')
            num = int(num)
            if num in produtos and produtos[num]['ativo'] :
                  print()
                  print(f'produto numero -> {num}')
                  print()
                  print(f'1 𓊯 nome -> {produtos[num]['produto']}')
                  print(f'2 𓊯 estoque -> {produtos[num]['estoque']}')
                  print(f'3 𓊯 preço -> R$ {produtos[num]['valor']}')
                  print()
                  produto = input('𓊯 digite o novo nome do produto para cadastrar : ')
                  estoque = input('𓊯 digite a nova quantidade que tem no estoque : ')
                  while not verifica_int(estoque):
                    print()
                    print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                    print()
                    estoque = input('🤍ྀི  digite a nova quantidade que tem no estoque : ')
                  estoque = int(estoque)
                  valor = input('𓊯 digite o novo preço do produto : ')
                  while not verifica_float(valor):
                    print()
                    print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                    print()
                    valor = input('🤍ྀི  digite o novo preço do produto : ')
                  valor = float(valor)
                  produtos[num] = {
                  'produto' : produto, 
                  'estoque' : estoque,
                  'valor' : valor,
                  'ativo' : True
                    }
                  print('produto editado com suscesso ! ')
                  input('tecle ENTER para continuar.....')
            else : 
                  print(f'produto numero {num} não encontrado')
                  input('tecle ENTER para continuar.....')

        elif resp2 == 4 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  EXCLUIR PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = input('digite o numero do produto que deseja excluir : ')
            while not verifica_int(num):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              num = input('🤍ྀི  digite o numero do produto que deseja excluir : ')
            num = int(num)
            if num in produtos :
                  print()
                  print(f'produto numero -> {num}')
                  print()
                  print(f' 𓊯 nome -> {produtos[num]['produto']}')
                  print(f' 𓊯 estoque -> {produtos[num]['estoque']}')
                  print(f' 𓊯 preço -> R$ {produtos[num]['valor']}')
                  print()
                  resp = input('deseja mesmo deletar esse produto ? [S/N] ')
                  if resp in 'sS' :
                    produtos[num]['ativo'] = False
                    print('produto excluido com suscesso')
                    input('pres ENTER para continuar....')
                  else :
                    print('operação canselada')
                    input('pres ENTER para continuar....')
            else : 
              print(f'produto numero {num} não encontrado')
              input('pres ENTER para continuar....')

    #módulo de pedidos         
        
    elif resp == 4 : 
        resp2 = ''
        while resp2 != 0 :
          os.system('cls')
          os.system('clear')
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅ MÓDULO DE CONSUMO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
          print()
          print('1 𓊯    resistrar pedido     𓊯')
          print('2 𓊯    consultar pedidos    𓊯')
          print('3 𓊯    cancelar pedidos     𓊯')
          print('0 𓊯         voltar          𓊯')
          print()
          resp2 = input('🤍ྀི  digite o numero da operação : ')
          while not verifica_int(resp2):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              resp2 = input('🤍ྀི  digite o numero da operação : ')
          resp2 = int(resp2)
          os.system('cls')
          os.system('clear')
          if resp2 == 1 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PEDIDO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = max(pedidos.keys()) + 1
            print(f'NUMERO DO PEDIDO -> {num}')
            print()
            hospedagem = input('𓊯 digite o numero da hospedagem : ')
            while not verifica_int(hospedagem):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              hospedagem = input('🤍ྀི  digite o numero da hospedagem : ')
            hospedagem = int(hospedagem)
            while hospedagem not in hospedagens or hospedagens[hospedagem]['status'] == 'fechado':
              print('! HOSPEDAGEM INVALIDDA !')
              hospedagem = int(input('𓊯 digite o numero da hospedagem : '))
            print()
            for chave, dados in produtos.items():
              print(f'|||   PRODUTO {chave:^5} |  NOME > {dados['produto']:^30}  |  PREÇO  >  R${dados['valor']:^10}  |  ESTOQUE  > {dados['estoque']:^10} |||')
            print()
            produto = input('𓊯 digite o numero do produto : ')
            while not verifica_int(produto):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              produto = input('🤍ྀི  digite o numero do produto : ')
            produto = int(produto)
            quantidade = input('𓊯 digite a quantidade que deseja : ')
            while not verifica_int(quantidade):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              quantidade = input('🤍ྀི  digite o numero do produto : ')
            quantidade = int(quantidade)
            if quantidade <= produtos[produto]['estoque'] :
              pedidos[num] = {
              'hospedagem' : hospedagem , 
              'produto'    : produto,
              'quantidade' : quantidade,
              'status' : 'em aberto',
              'ativo' : True ,
                            }
              produtos[produto]['estoque'] = produtos[produto]['estoque'] - quantidade
              print('pedido cadastrado com sucesso')
              input('tecle o ENTER para continuar.....')
            else :
              print()
              print('! ESTOQUE INSUFICIENTE PARA QUANTIDADE DO PEDIDO !')
              input('tecle o ENTER para continuar.....')
        
          elif resp2 == 2 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            print('1 ָ☾. listar todas')
            print('2 ָ☾. buscar por hospedagem')
            print('3 ָ☾. buscar por pedido')
            print()
            resp3 = input('🤍ྀི  digite o numero da operação : ')
            while not verifica_int(resp3):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              resp3 = input('🤍ྀི  digite o numero da operação : ')
            resp3 = int(resp3)

            if resp3 == 1 :
              print()
              print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
              print()
              for chave, dados in pedidos.items() :
                if dados['ativo'] :
                  print()
                  print('☕︎ 𓎩 ‧₊˚'*15)
                  print()
                  print(f'pedido numero -> {chave}')
                  print()
                  print(f'𓊯 hospedagem -> {dados['hospedagem']}')
                  print(f'𓊯 produto -> {produtos[dados['produto']]['produto']}')
                  print(f'𓊯 quantidade -> {dados['quantidade']}')
                  print(f'𓊯 status -> {dados['status']}')
              print()
              print('☕︎ 𓎩 ‧₊˚'*15)
              print()
              input('tecle ENTER para continuar.....')
            
            elif resp3 == 2 :
              print()
              print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE CONSUMO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
              print()
              num = input('digite o numero da hospedagem que deseja consultar os pedidos : ')
              while not verifica_int(num):
                print()
                print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                print()
                num = input('🤍ྀི  digite o numero da hospedagem que deseja consultar os pedidos : ')
              num = int(num)
              if num not in hospedagens :
                print()
                print('! HOSPDAGEM NÃO ENCONTRADA !')
                print()
                input('tecle ENTER para continuar......')
              else :
                encontrou = False
                total = 0
                for i in range(1,len(pedidos)+1) :
                  if pedidos[i]['hospedagem'] == num :
                    print()
                    print('☕︎ 𓎩 ‧₊˚'*15)
                    print()
                    print(f'pedido numero -> {i}')
                    print()
                    print(f'𓊯 hospedagem -> {pedidos[i]['hospedagem']}')
                    print(f'𓊯 produto -> {produtos[pedidos[i]['produto']]['produto']}')
                    print(f'𓊯 quantidade -> {pedidos[i]['quantidade']}')
                    print(f'𓊯 status -> {pedidos[i]['status']}')
                    encontrou = True
                    total += produtos[pedidos[i]['produto']]['valor'] * pedidos[i]['quantidade']
                print() 
                print('☕︎ 𓎩 ‧₊˚'*15)
                print()
                if encontrou :
                  print(F'TOTAL A PAGAR POR CONSUMO HOSPEGAEM NUMERO {num} : ')
                  print(f'total -> R${total:.2f}')
                else :
                  print(f'nem um pedido cadastrado na hospedagem {num}')
                input('tecle ENTER para continuar......')
            elif resp3 == 3:
              print()
              print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE CONSUMO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
              print()
              num = input('digite o numero do pedido que deseja consultar : ')
              while not verifica_int(num):
                print()
                print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                print()
                num = input('🤍ྀི  digite o numero do pedido que deseja consultar : ')
              num = int(num)
              if num in pedidos and pedidos[num]['ativo'] :
                  print()
                  print(f'pedido numero -> {num}')
                  print()
                  print(f'𓊯 hospedagem -> {pedidos[num]['hospedagem']}')
                  print(f'𓊯 produto -> {produtos[pedidos[num]['produto']]['produto']}')
                  print(f'𓊯 quantidade -> {pedidos[num]['quantidade']}')
                  print(f'𓊯 status -> {pedidos[num]['status']}')
                  print()  
                  input('pres ENTER para continuar....')
              else : 
                print(f'pedido numero {num} não encontrado')
                input('pres ENTER para continuar....')

          elif resp2 == 3 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CANCELAR PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = input('digite o numero do pedido que deseja cancelar : ')
            while not verifica_int(num):
                print()
                print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
                print()
                num = input('🤍ྀི  digite o numero do pedido que deseja cancelar : ')
            num = int(num)
            if num in pedidos and pedidos[num]['ativo'] : 
              if pedidos[num]['status'] == 'em aberto' :
                  print()
                  print(f'pedido numero -> {num}')
                  print()
                  print(f'𓊯 hospedagem -> {pedidos[num]['hospedagem']}')
                  print(f'𓊯 produto -> {produtos[pedidos[num]['produto']]['produto']}')
                  print(f'𓊯 quantidade -> {pedidos[num]['quantidade']}')
                  print(f'𓊯 status -> {pedidos[num]['status']}')
                  print()
                  resp = input('deseja mesmo cancelar esse pedido ? [S/N] ')
                  if resp in 'sS' :
                    pedidos[num]['ativo'] = False
                    print('pedido cancelado com suscesso')
                    input('pres ENTER para continuar....')
                  else :
                    print('operação canselada')
              else : 
                print(f'pedido numero {num} ja foi pago')
                input('pres ENTER para continuar....')
            else : 
              print(f'pedido numero {num} não encontrado')
              input('pres ENTER para continuar....')
                    
      
    # módulo de relatorio
      
    elif resp == 5 :
      print()
      print('-ˋˏ✄┈┈┈┈ MÓDULO DE RELATORIO -ˋˏ✄┈┈┈┈')
      print()
      print('1 ╰┈➤ relatorio de suites ')
      print('2 ╰┈➤ relatorio de hospedagens  ')
      print('3 ╰┈➤ relatorio de consumo ')
      print('4 ╰┈➤ relatorio de pedidos ')
      print('0 ╰┈➤ voltar ')
      print()
      resp2 = int(input('🤍ྀི digite o numero da operação : '))
    
  
    # módulo de informação 

    elif resp == 6 :
      print()
      print('   ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘ MÓDULO DE INFORMAÇÃO ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')
      print()
      print('🕷       projeto de sistema de gestão para moteis     🕷')
      print('🕷  desenvolvedor ➜ Lucas Antonio Florentino Barbosa 🕷')
      print('🕷            Licença Pública Geral GNU               🕷')
      print('🕷           www.gnu.org/licenses/gpl.html            🕷')
      print()
      input('🕷  tecle ENTER para continuar....')

print()
print('········· FIM DO PROGRAMA ·········')

   # salvamento de dados  
 
salva_suites(suites)
 
salva_hospedagens(hospedagens)

salva_produtos(produtos)

salva_pedidos(pedidos)
