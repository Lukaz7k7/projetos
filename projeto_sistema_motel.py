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
      suites[num] = [tipo, valor, status]
  arq_suites.close()

except : 
  suites = {
        1 : ['premiun',69.0,'ocupado'],
        2 : ['simplees', 24.0, 'ocupado'],
        3 : ['luxo', 45.50 , 'livre']
  }
  arq_suites = open('suites.txt','wt',encoding="utf-8")
  for num, dados in suites.items() :
      arq_suites.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
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
      entrada = dados[2]
      cpf = int(dados[3])
      status = dados[4]
      if dados[4] == 'fechado':
        saida = dados[5]
        valor_t = float(dados[6])
        hospedagens[num] = [suite,entrada,cpf,status,saida,valor_t]
      else:
        hospedagens[num] = [suite,entrada,cpf,status]
  arq_hospedagens.close

except:
  hospedagens = {
    1 : [1, datetime(2026, 6, 13, 15, 30, 42) , 10531031403 , 'em aberto' ],
    2 : [2, datetime(2026, 6, 13, 15, 30, 42) , 10531031403 , 'em aberto' ]
  }
  arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
  for chave,dados in hospedagens.items() : 
    if dados[3] == 'fechado' :
      arq_hospedagens.write(f'{num},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n')
    else :
      arq_hospedagens.write(f'{num},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n')
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
      produtos[num] = [produto, estoque, valor]
  arq_produtos.close()

except : 
  produtos = {
  1 : ['vinho', 20 , 50.0 ],
  2 : ['lubrificante', 15, 5.5],
  3 : ['camisinha', 30 , 5.5 ]
  }
  arq_produtos = open('produtos.txt','wt',encoding="utf-8")
  for num, dados in produtos.items() :
      arq_produtos.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
  arq_produtos.close()

pedidos = {}
try : 
  arq_pedidos = open('pedidos.txt','rt', encoding="utf-8")
  for linha in arq_pedidos : 
    linha = linha.strip()
    if linha :
      dados = linha.split(',')
      num = int(dados[0])
      suite = int(dados[1])
      produto = int(dados[2])
      quantidade = int(dados[3])
      pedidos[num] = [suite, produto, quantidade]
  arq_pedidos.close()

except : 
  pedidos = { 
  1 : [1,2,1],
  2 : [1,1,4],
  3 : [2,1,4],
  4 : [2,1,4],
  5 : [2,1,4]
  }
  arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
  for num, dados in pedidos.items() :
      arq_pedidos.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
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
    resp = int(input('🤍ྀི   digite sua resposta : '))
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
        print('4 ☪︎  excluir suíte    ☪︎')
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
          suites[numero_s] = [tipo_s, valor_s, 'livre']
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
                print()
                print(f'SUÍTE NUMERO -> {chave}')
                print(f'tipo -> {dados[0]}')
                print(f'valor por hora -> R${dados[1]}')
                print(f'status -> {dados[2]}')
                print()
                print('☪-☪'*25)

            print()
            input('tecle ENTER para continuar ....')
          else : 
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            num = int(input('digite o numero da suíte que deseja consultar : '))
            if num in suites :
              print()
              print(f'☪ numero -> {num}')
              print(f'☪ tipo -> {suites[num][0]}')
              print(f'☪ valor por hora -> {suites[num][1]}')
              print(f'☪ status -> {suites[num][2]}')
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
            if suites[num][2] != "ocupado" :
                tipo_s = input('☪ escolha o tipo da suíte [1-simples / 2-luxo / 3-premium] : ')
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
                suites[num] = [tipo_s, valor_s, 'livre']
                print('suíte editada com suscesso')
                input('pres ENTER para continuar....')
            else:
                print(f'suíte numero {num} não pode ser editada pois está em uso')
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
          if num in suites :
                if suites[num][2] != "ocupado" :
                  print(f'☪ numero -> {num}')
                  print(f'☪ tipo -> {suites[num][0]}')
                  print(f'☪ valor por hora -> {suites[num][1]}')
                  print(f'☪ status -> {suites[num][2]}')
                  print()
                  respd = input('deseja mesmo deletar essa suíte ? [S/N] ')
                  if respd == 's' or respd == 'S' :
                    del(suites[num])
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
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-IN ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          for i in range(1,(len(suites)+1)):
            if 'livre' in suites[i] : 
              print(f'suíte {i} : ',suites[i],end=' -=- ')
          print()
          print()
          id_hospedagem = len(hospedagens)+1
          print(f'NUMERO DA SUA HOSPEDAGEM -> {id_hospedagem}')
          print()
          suite = int(input('ָ☾. digite o numero da suite que deseja : '))
          while suite not in suites or suites[suite][2] != "livre" :
              print('suíte invalida, digite uma suíte disponivel.')
              suite = int(input('ָ☾. digite o numero da suite que deseja : '))
          cpf = int(input('ָ☾. digite o seu CPF : '))
          entrada = datetime.now()
          print()
          hospedagens[id_hospedagem] = [suite,entrada,cpf,'em aberto']
          suites[suite][2] = 'ocupado'
          print('check-in feita com suscesso ! ')
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
              print(f'SUITE -> {dados[0]}')
              print(f'ENTRADA -> {dados[1]}')
              print(f'CPF -> {dados[2]}')
              print(f'STATUS -> {dados[3]}')
              if dados[3] == 'fechado' :
                print(f'SAÍDA -> {dados[4]}')
                print(f'VALOR TOTAL -> {dados[5]}')
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
              print(f'SUITE -> {hospedagens[num][0]}')
              print(f'ENTRADA -> {hospedagens[num][1]}')
              print(f'CPF -> {hospedagens[num][2]}')
              print(f'STATUS -> {hospedagens[num][3]}')
              if hospedagens[num][3] == 'fechado' :
                print(f'SAÍDA -> {hospedagens[num][4]}')
                print(f'VALOR TOTAL -> {hospedagens[num][5]}')
              print()
              print('☪-☪'*25)
              print()
              input('tecle ENTER para continuar ....')
            else :
              print(f'suíte numero {num} não encontrada')
              input('pres ENTER para continuar....')
      
        elif resp2 == 3 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-OUT ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da hospedagem : '))
          if num in hospedagens:
            saida = datetime.now()
            print()
            hospedagens[num].append(saida)
            print()
            print(f'☾. numero -> {num}')
            print(f'ָ☾. suíte -> {hospedagens[num][0]}')
            print(f'ָ☾. entrada -> {hospedagens[num][1]}')
            print(f'ָ☾. CPF -> {hospedagens[num][2]}')
            print(f'ָ☾. status -> {hospedagens[num][3]}')
            print(f'ָ☾. saida -> {hospedagens[num][4]}')
            tempo_t = hospedagens[num][4] - hospedagens[num][1]
            tempo_t = tempo_t.total_seconds() / 3600
            valor_hospedagem = tempo_t * suites[hospedagens[num][0]][1]
            print(f'ָ☾. valor da hospedagem -> R${valor_hospedagem:.2f}')

            valor_consumo = 0
            for i in range(1,len(pedidos)+1) :
              if pedidos[i][0] == num :
                 valor_consumo += produtos[pedidos[i][1]][2] * pedidos[i][2]

            print(f'ָ☾. valor de consumo -> R${valor_consumo}')  
            print(f'ָ☾. valor total -> R${valor_consumo + valor_hospedagem :.2f} ')
            print()
            suite = hospedagens[num][0]
            resp4 = input('dejeja fechar essa hospedagem ? [S/N] ')
            if resp4 in 'Ss' :
              suites[suite][2] = 'livre'
              hospedagens[num][3] = 'fechado'
              hospedagens[num].append(valor_hospedagem)
              print('check-out realizado com suscesso !')
            else :
              print('check-out cancelado')
              del(hospedagens[num][4])
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
        print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅ MÓDULO DE PRODUTOS E CONSUMO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
        print()
        print('1 𓊯   cadastrar produstos   𓊯')
        print('2 𓊯      ver produtos       𓊯')
        print('3 𓊯     editar produto      𓊯')
        print('4 𓊯     excluir produto      𓊯')
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
          nome = input('𓊯 digite o nome do produto para cadastrar : ')
          quant = int(input('𓊯 digite a quantidade que tem no estoque : '))
          preco = float(input('𓊯 digite o preço do produto : '))
          produtos[num] = [nome,quant,preco]
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
              print()
              print('☕︎ 𓎩 ‧₊˚'*15)
              print()
              print(f'produto numero -> {chave}')
              print()
              print(f'𓊯 nome -> {dados[0]}')
              print(f'𓊯 estoque -> {dados[1]}')
              print(f'𓊯 preço -> R$ {dados[2]}')
            print()
            print('☕︎ 𓎩 ‧₊˚'*15)
            print()
            input('tecle ENTER para continuar.....')
          
          else :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = int(input('digite o numero do produto que deseja consultar : '))
            if num in produtos :
              print()
              print(f'produto numero -> {num}')
              print()
              print(f'𓊯 nome -> {produtos[num][0]}')
              print(f'𓊯 estoque -> {produtos[num][1]}')
              print(f'𓊯 preço -> R$ {produtos[num][2]}')
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
            if num in produtos :
                  print()
                  print(f'produto numero -> {num}')
                  print()
                  print(f'1 𓊯 nome -> {produtos[num][0]}')
                  print(f'2 𓊯 estoque -> {produtos[num][1]}')
                  print(f'3 𓊯 preço -> R$ {produtos[num][2]}')
                  print()
                  editar_p = (int(input('digite o numero do que quer editar : '))-1)
                  while editar_p not in [1,2,3] :
                    print('resposta invalida, digite uma resposta valida !')
                    editar_p = (int(input('digite o numero do que quer editar : '))-1)

                  if editar_p == 0 :
                    editar = input('digite a nova informação : ')
                  elif editar_p == 1 :
                    editar = int(input('digite a nova informação : '))
                  else:
                    editar = float(input('digite a nova informação : '))
                  produtos[num][editar_p] = editar
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
                  print(f' 𓊯 nome -> {produtos[num][0]}')
                  print(f' 𓊯 estoque -> {produtos[num][1]}')
                  print(f' 𓊯 preço -> R$ {produtos[num][2]}')
                  print()
                  resp = input('deseja mesmo deletar esse produto ? [S/N] ')
                  if resp in 'sS' :
                    del(produtos[num])
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
            hospedagem = int(input('𓊯 digite o numero da hospedagem : '))
            produto = int(input('𓊯 digite o numero do produto : '))
            quantidade = int(input('𓊯 digite a quantidade que deseja : '))
            pedidos[num] = [hospedagem,produto,quantidade]
            print('pedido cadastrado com sucesso')
            input('tecle o ENTER para continuar.....')
        
          elif resp2 == 2 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            print('1 ָ☾. listar todas')
            print('2 ָ☾. buscar por hospedagem')
            print()
            resp3 = int(input('🤍ྀི  digite o numero da operação : '))

            if resp3 == 1 :
              print()
              print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
              print()
              for chave, dados in pedidos.items() :
                print()
                print('☕︎ 𓎩 ‧₊˚'*15)
                print()
                print(f'pedido numero -> {chave}')
                print()
                print(f'𓊯 hospedagem -> {dados[0]}')
                print(f'𓊯 produto -> {produtos[dados[1]][0]}')
                print(f'𓊯 quantidade -> {dados[2]}')
              print()
              print('☕︎ 𓎩 ‧₊˚'*15)
              print()
              input('tecle ENTER para continuar.....')
            
            else :
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
                  if pedidos[i][0] == num :
                    print()
                    print('☕︎ 𓎩 ‧₊˚'*15)
                    print()
                    print(f'pedido numero -> {i}')
                    print()
                    print(f'𓊯 hospedagem -> {pedidos[i][0]}')
                    print(f'𓊯 produto -> {produtos[pedidos[i][1]][0]}')
                    print(f'𓊯 quantidade -> {pedidos[i][2]}')
                    encontrou = True
                    total += produtos[pedidos[i][1]][2] * pedidos[i][2]
                print() 
                print('☕︎ 𓎩 ‧₊˚'*15)
                print()
                if encontrou :
                  print(F'TOTAL A PAGAR POR CONSUMO HOSPEGAEM NUMERO {num} : ')
                  print(f'total -> R${total}')
                else :
                  print(f'nem um pedido cadastrado na hospedagem {num}')
                input('tecle ENTER para continuar......')
                    
      
    # módulo de relatorio
      
    elif resp == 5 :
      print()
      print('-ˋˏ✄┈┈┈┈ MÓDULO DE RELATORIO -ˋˏ✄┈┈┈┈')
      print()
      print('1 ╰┈➤ relatorio de suites ocupadas')
      print('2 ╰┈➤ relatorio de hospedagens  ')
      print('3 ╰┈➤ relatorio de pedidos ')
      print('4 ╰┈➤ relatorio de faturamento ')
      print('5 ╰┈➤ relatorio de estoque ')
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
    arq_suites.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
arq_suites.close()

arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
for chave,dados in hospedagens.items() : 
  if dados[3] == 'fechado' :
    arq_hospedagens.write(f'{num},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n')
  else :
    arq_hospedagens.write(f'{num},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n')
arq_hospedagens.close()

arq_produtos = open('produtos.txt','wt',encoding="utf-8")
for num, dados in produtos.items() :
    arq_produtos.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
arq_produtos.close()

arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
for num, dados in pedidos.items() :
    arq_pedidos.write(f'{num},{dados[0]},{dados[1]},{dados[2]}\n')
arq_pedidos.close()