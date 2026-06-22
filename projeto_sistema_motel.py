import os , time 
from datetime import datetime

   # recuperando dados dos arquivos
suites = {}
try : 
        arq_suites = open('suites.txt','rt', encoding="utf-8")
        for linha in arq_suites : 
            linha = linha.strip()
            if linha :
                dados = linha.split(',')
                num = int(dados[0])
                tipo = dados[1]
                valor = float(dados[2])
                status = dados[3]
                ativo = dados[4] == "True"
                suites[num] = {
                    'tipo' : tipo, 
                    'valor' : valor,
                    'status' : status,
                    'ativo' : ativo
                    }
        arq_suites.close()

except : 
    suites = {

            1 : {
            'tipo' : 'premiun',
            'valor' : 69.0,
            'status': 'ocupado',
            'ativo' : True,
            },

            2 : {
            'tipo'  : 'simples',
            'valor' : 24.0,
            'status': 'ocupado',
            'ativo' : True,
            },
            3 : {
            'tipo'  : 'luxo',
            'valor' : 45.50,
            'status': 'livre',
            'ativo' : True,
            },
        }
    arq_suites = open('suites.txt','wt',encoding="utf-8")
    for num, dados in suites.items() :
        arq_suites.write(f'{num},{dados['tipo']},{dados['valor']},{dados['status']},{dados['ativo']}\n')
    arq_suites.close()

hospedagens = {}
try : 
        arq_hospedagens = open('hospedagens.txt','rt',encoding="utf-8")
        for linha in arq_hospedagens :
            linha = linha.strip()
            if linha: 
                dados = linha.split(',')
                num = int(dados[0])
                suite = int(dados[1])
                entrada = datetime.fromisoformat(dados[2])
                cpf = int(dados[3])
                status = dados[4]
                if dados[4] == 'fechado':
                    saida = datetime.fromisoformat(dados[5])
                    valor_t = float(dados[6])
                    hospedagens[num] = {
                    'suite' : suite,
                    'entrada' : entrada,
                    'cpf' : cpf,
                    'status' : status,
                    'saida' : saida,
                    'valor_t' : valor_t,
                        }
                else:
                    hospedagens[num] = {
                    'suite' : suite,
                    'entrada' : entrada,
                    'cpf' : cpf,
                    'status' : status,
                    }
        arq_hospedagens.close()

except:
    hospedagens = {
        1 : {
        'suite' : 1, 
        'entrada' : datetime(2026, 6, 13, 15, 30, 42) ,
        'cpf' :  10531031403 ,
        'status' :  'em aberto',
        },
        2 : {
        'suite' : 2, 
        'entrada' : datetime(2026, 6, 13, 15, 30, 42) ,
        'cpf' :  10531031403 ,
        'status' :  'em aberto',
            },
        }
    arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
    for num,dados in hospedagens.items() : 
        if dados['status'] == 'fechado' :
            arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']},{dados['saida']},{dados['valor_t']}\n')
        else :
            arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']}\n')
    arq_hospedagens.close()

produtos = {}
try : 
        arq_produtos = open('produtos.txt','rt', encoding="utf-8")
        for linha in arq_produtos : 
            linha = linha.strip()
            if linha :
                dados = linha.split(',')
                num = int(dados[0])
                produto = dados[1]
                estoque = int(dados[2])
                valor = float(dados[3])
                ativo = dados[4] == "True"
                produtos[num] = {
                    'produto' : produto, 
                    'estoque' : estoque,
                    'valor' : valor,
                    'ativo' : ativo
                        }
        arq_produtos.close()

except : 
    produtos = {
        1 : {
            'produto' : 'vinho', 
            'estoque' : 20 ,
            'valor' :  50.0 ,
            'ativo' : True ,
            },
        2 : {
            'produto' : 'lubrificante',
            'estoque' : 15,
            'valor' :  5.5,
            'ativo' : True ,
            },
        3 : {
            'produto' : 'camisinha',
            'estoque' : 15,
            'valor' :  5.5,
            'ativo' : True ,
            },
            }
    arq_produtos = open('produtos.txt','wt',encoding="utf-8")
    for num, dados in produtos.items() :
        arq_produtos.write(f'{num},{dados['produto']},{dados['estoque']},{dados['valor']},{dados['ativo']}\n')
    arq_produtos.close() 

pedidos = {}
try : 
        arq_pedidos = open('pedidos.txt','rt', encoding="utf-8")
        for linha in arq_pedidos : 
            linha = linha.strip()
            if linha :
                dados = linha.split(',')
                num = int(dados[0])
                hospedagem = int(dados[1])
                produto = int(dados[2])
                quantidade = int(dados[3])
                status = dados[4]
                ativo = dados[5] == "True"
                pedidos[num] = {
                    'hospedagem' : hospedagem , 
                    'produto' : produto,
                    'quantidade' : quantidade,
                    'status' : status,
                    'ativo' : ativo,
                    }
        arq_pedidos.close()

except : 
        pedidos = { 
        1 : {
            'hospedagem' : 1,
            'produto' : 2,
            'quantidade' : 1,
            'status' : 'em aberto',
            'ativo' : True,
            },
        2 : {
            'hospedagem' : 1,
            'produto' : 1,
            'quantidade' : 4,
            'status' : 'em aberto',
            'ativo' : True,
            },
        3 : {
            'hospedagem' : 2,
            'produto' : 1,
            'quantidade' : 4,
            'status' : 'em aberto',
            'ativo' : True,
            },
        4 : {
            'hospedagem' : 2,
            'produto' : 1,
            'quantidade' : 4,
            'status' : 'em aberto',
            'ativo' : True,
            },
        5 : {
            'hospedagem' : 2,
            'produto' : 1,
            'quantidade' : 4,
            'status' : 'em aberto',
            'ativo' : True,
                    },
                }
        arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
        for num, dados in pedidos.items() :
            arq_pedidos.write(f'{num},{dados['hospedagem']},{dados['produto']},{dados['quantidade']},{dados['status']},{dados['ativo']}\n')
        arq_pedidos.close()


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
    while not resp.isnumeric():
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
        print()
        print('✩₊˚.⋆☾⋆⁺₊✧ MÓDUULO DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
        print()
        print('1 ☪︎ cadastrar suítes ☪︎')
        print('2 ☪︎ consultar suítes ☪︎')
        print('3 ☪︎  editar suítes   ☪︎')
        print('4 ☪︎  excluir suíte   ☪︎')
        print('0 ☪︎     voltar       ☪︎')
        print()
        resp2 = int(input('🤍ྀི  digite o numero da operação : '))
        os.system('cls')
        os.system('clear')
        if resp2 == 1 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ CADASTRAR SUÍTE ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          numero_s = max(suites.keys()) + 1
          print(f'☪ número da suíte => {numero_s}')
          tipo_s = int(input('☪ escolha o tipo da suite [1-simples / 2-luxo / 3-premium] : '))
          while tipo_s not in [1,2,3] :
            print('numero invalido, escolha um numero valido')
            tipo_s = int(input('☪ escolha o tipo da suíte [1-simples / 2-luxo / 3-premium] : '))
          match tipo_s :
            case 1:
              tipo_s = 'simples'
            case 2 :
              tipo_s = 'luxo'
            case 3 :
              tipo_s = 'premium'

          valor_s = float(input('☪ informe o valor por hora : R$ '))
          print()
          suites[numero_s] = {
            'tipo' : tipo_s, 
            'valor': valor_s,
            'status': 'livre',
            'ativo': True
            }
          print('suíte cadastrada com suscesso !')
          input('pres ENTER para continuar...')

        elif resp2 == 2 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ CONSULTAR SUÍTE ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          print('1 ☪︎ listar todas')
          print('2 ☪︎ buscar por numero')
          print()
          resp3 = int(input('🤍ྀི  digite o numero da operação : '))
          if resp3 == 1 :
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ LISTAGEM DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            print('☪-☪'*25)
            for chave, dados in suites.items() :
              if dados['ativo']:
                print()
                print(f'SUÍTE NUMERO -> {chave}')
                print(f'tipo -> {dados['tipo']}')
                print(f'valor por hora -> R${dados['valor']}')
                print(f'status -> {dados['status']}')
                print()
                print('☪-☪'*25)

            print()
            input('tecle ENTER para continuar ....')
          else : 
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            num = int(input('digite o numero da suíte que deseja consultar : '))
            if num in suites and suites[num]['ativo'] :
              print()
              print(f'☪ numero -> {num}')
              print(f'☪ tipo -> {suites[num]['tipo']}')
              print(f'☪ valor por hora -> {suites[num]['valor']}')
              print(f'☪ status -> {suites[num]['status']}')
              print()
              input('tecle ENTER para continuar .....')
            else :
              print(f'suíte numero {num} não encontrada')
              input('pres ENTER para continuar....')

        elif resp2 == 3  :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EDIÇÃO DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da suíte que deseja editar : '))
          if num in suites :
            if suites[num]['status'] != "ocupado" and suites[num]['ativo'] :
                tipo_s = int(input('☪ escolha o tipo da suíte [1-simples / 2-luxo / 3-premium] : '))
                while tipo_s not in [1,2,3] :
                  print('numero invalido, escolha um numero valido')
                  tipo_s = int(input('☪ escolha o tipo da suíte [1-simples / 2-luxo / 3-premium] : '))
                match tipo_s :
                  case 1:
                    tipo_s = 'simples'
                  case 2 :
                    tipo_s = 'luxo'
                  case 3 :
                    tipo_s = 'premium'

                valor_s = float(input('☪ valor por hora : R$ '))
                suites[num] = suites[numero_s] = {
                        'tipo' : tipo_s, 
                        'valor': valor_s,
                        'status': 'livre',
                        'ativo': True
                      }
                print('suíte editada com suscesso')
                input('pres ENTER para continuar....')
            else:
                print(f'suíte numero {num} não pode ser editada pois está em uso ou desativada')
                input('pres ENTER para continuar....')
          else :
                print(f'suíte numero {num} não encontrada')
                input('pres ENTER para continuar....')
          
                
        elif resp2 == 4 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EXCLUIR SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da suíte que deseja excluir : '))
          print()
          if num in suites and suites[num]['ativo'] :
                if suites[num]['status'] != "ocupado" :
                  print(f'☪ numero -> {num}')
                  print(f'☪ tipo -> {suites[num]['tipo']}')
                  print(f'☪ valor por hora -> {suites[num]['valor']}')
                  print(f'☪ status -> {suites[num]['status']}')
                  print()
                  respd = input('deseja mesmo deletar essa suíte ? [S/N] ')
                  if respd == 's' or respd == 'S' :
                    suites[num]['ativo'] = False 
                    print('suíte excluida com suscesso')
                    input('pres ENTER para continuar....')
                  else :
                    print('operação canselada')
                    input('pres ENTER para continuar....')
                else :
                  print(f'suíte numero {num} não pode ser deletada pois está em uso')
                  input('pres ENTER para continuar....')
          else : 
                print(f'suíte numero {num} não encontrada')
                input('pres ENTER para continuar....')

    # módulo de hospedagem        

    elif resp == 2 :
      resp2 = ''
      while resp2 != 0:
        os.system('cls')
        os.system('clear')
        print()
        print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
        print()
        print('1 ࣪ ִֶָ☾.   Fazer check-in     ࣪ ִֶָ☾.')
        print('2 ࣪ ִֶָ☾. consultar hospedagem ࣪ ִֶָ☾.')
        print('3 ࣪ ִֶָ☾.   Fazer check-out    ࣪ ִֶָ☾.')
        print('0 ࣪ ִֶָ☾.       voltar         ࣪ ִֶָ☾.')
        print()
        resp2 = int(input('🤍ྀི  digite o numero da operação : ')) 
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
              suite = int(input('ָ☾. digite o numero da suite que deseja : '))
              while suite not in suites or (suites[suite]['status'] != "livre" and suites[suite]['ativo'] == False) :
                  print('suíte invalida, digite uma suíte disponivel.')
                  suite = int(input('ָ☾. digite o numero da suite que deseja : '))
              cpf = int(input('ָ☾. digite o seu CPF : '))
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
          resp3 = int(input('🤍ྀི  digite o numero da operação : '))
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
            num = int(input('digite o numero da hospedagem que deseja consultar : '))
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
          num = int(input('digite o numero da hospedagem : '))
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
        resp2 = int(input('🤍ྀི  digite o numero da operação : '))
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
          estoque = int(input('𓊯 digite a quantidade que tem no estoque : '))
          valor = float(input('𓊯 digite o preço do produto : '))
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
          resp3 = int(input('🤍ྀི  digite o numero da operação : '))
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
            num = int(input('digite o numero do produto que deseja consultar : '))
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
            num = int(input('digite o numero do produto que deseja editar : '))
            if num in produtos and produtos[num]['ativo'] :
                  print()
                  print(f'produto numero -> {num}')
                  print()
                  print(f'1 𓊯 nome -> {produtos[num]['produto']}')
                  print(f'2 𓊯 estoque -> {produtos[num]['estoque']}')
                  print(f'3 𓊯 preço -> R$ {produtos[num]['valor']}')
                  print()
                  produto = input('𓊯 digite o novo nome do produto para cadastrar : ')
                  estoque = int(input('𓊯 digite a nova quantidade que tem no estoque : '))
                  valor = float(input('𓊯 digite o novo preço do produto : '))
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
            num = int(input('digite o numero do produto que deseja excluir : '))
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
          resp2 = int(input('🤍ྀི  digite o numero da operação : '))
          os.system('cls')
          os.system('clear')
          if resp2 == 1 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PEDIDO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = max(pedidos.keys()) + 1
            print(f'NUMERO DO PEDIDO -> {num}')
            print()
            hospedagem = int(input('𓊯 digite o numero da hospedagem : '))
            while hospedagem not in hospedagens or hospedagens[hospedagem]['status'] == 'fechado':
              print('! HOSPEDAGEM INVALIDDA !')
              hospedagem = int(input('𓊯 digite o numero da hospedagem : '))
            print()
            for chave, dados in produtos.items():
              print(f'|||   PRODUTO {chave:^5} |  NOME > {dados['produto']:^30}  |  PREÇO  >  R${dados['valor']:^10}  |  ESTOQUE  > {dados['estoque']:^10} |||')
            print()
            produto = int(input('𓊯 digite o numero do produto : '))
            quantidade = int(input('𓊯 digite a quantidade que deseja : '))
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
        
          elif resp2 == 2 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            print('1 ָ☾. listar todas')
            print('2 ָ☾. buscar por hospedagem')
            print('3 ָ☾. buscar por pedido')
            print()
            resp3 = int(input('🤍ྀི  digite o numero da operação : '))

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
              num = int(input('digite o numero da hospedagem que deseja consultar os pedidos : '))
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
              num = int(input('digite o numero do pedido que deseja consultar : '))
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
            num = int(input('digite o numero do pedido que deseja cancelar : '))
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
 
arq_suites = open('suites.txt','wt',encoding="utf-8")
for num, dados in suites.items() :
    arq_suites.write(f'{num},{dados['tipo']},{dados['valor']},{dados['status']},{dados['ativo']}\n')
arq_suites.close()
 

arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
for num,dados in hospedagens.items() : 
  if dados['status'] == 'fechado' :
      arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']},{dados['saida']},{dados['valor_t']}\n')
  else :
      arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']}\n')
arq_hospedagens.close()

arq_produtos = open('produtos.txt','wt',encoding="utf-8")
for num, dados in produtos.items() :
    arq_produtos.write(f'{num},{dados['produto']},{dados['estoque']},{dados['valor']},{dados['ativo']}\n')
arq_produtos.close()

arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
for num, dados in pedidos.items() :
    arq_pedidos.write(f'{num},{dados['hospedagem']},{dados['produto']},{dados['quantidade']},{dados['status']},{dados['ativo']}\n')
arq_pedidos.close()
