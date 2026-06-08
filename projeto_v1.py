import os , time
suites = {
  1 : ['premiun',69.0,'ocupado'],
  2 : ['simplees', 24.0, 'livre'],
  3 : ['luxo', 45.50 , 'livre']
        }
hospedagens = {
  1 : [1, '12/03/2027' , '22:23:00', 'em aberto' ]
}
produtos = {
  1 : ['vinho', 20 , 50.0 ],
  2 : ['lubrificante', 15, 5.5],
  3 : ['camisinha', 30 , 5.5 ]
}
consumo = {
  1 : [1,1,1]
}
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
    print('3 ❥ módolo produtos e consumo')
    print('4 ❥ módolo de relatorio ')
    print('5 ❥ módolo de informações')
    print('0 ❥ sair ')
    print()
    resp = int(input('🤍ྀི   digite sua resposta : '))
    os.system('cls')
    os.system('clear')

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
          numero_s = (len(suites)+1) 
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
            for i in range(1,len(suites)+1):

                print(f'☪ numero -> {i}')
                print(f'☪ tipo -> {suites[i][0]}')
                print(f'☪ valor por hora -> {suites[i][1]}')
                print(f'☪ status -> {suites[i][2]}')
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
            print(f'☪ numero -> {num}')
            print(f'☪ tipo -> {suites[num][0]}')
            print(f'☪ valor por hora -> {suites[num][1]}')
            print(f'☪ status -> {suites[num][2]}')
            print()
            resp = input('deseja mesmo deletar essa suíte ? [S/N] ')
            if resp in 'sS' :
              del(suites[num])
              print('suíte excluida com suscesso')
              input('pres ENTER para continuar....')
            else :
              print('operação canselada')
              input('pres ENTER para continuar....')
          else : 
            print(f'suíte numero {num} não encontrada')
            input('pres ENTER para continuar....')

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
        print('3 ࣪ ִֶָ☾.  editar hospedagem   ࣪ ִֶָ☾.')
        print('4 ࣪ ִֶָ☾.   Fazer check-out    ࣪ ִֶָ☾.')
        print('5 ࣪ ִֶָ☾.  excluir hospodegem  ࣪ ִֶָ☾.')
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
          suite = int(input('ָ☾. digite o numero da suite que deseja : '))
          data = input('digite a data de entrada xx/xx/xxxx : ')
          hora = input('digite a hora de entrada xx:xx : ')
          print()
          hospedagens[len(hospedagens)+1] = [suite,data,hora,'em aberto']
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
            for i in range(1,len(hospedagens)+1):
              print()
              print('☪-☪'*25)
              print()
              print(f'hospedagem numero -> {i}')
              for j in range(1,len(hospedagens[i])):
                print(hospedagens[i][j])
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
              print(f'hospedagem numero -> {num}')
              for j in range(1,len(hospedagens[num])):
                print(hospedagens[i][j])
              input('tecle ENTER para continuar .....')
            else :
              print(f'suíte numero {num} não encontrada')
              input('pres ENTER para continuar....')
        elif resp2 == 3  :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EDIÇÃO DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da hospedagem que deseja editar : '))
          if num in suites :
            print()
            print(f'☾. numero -> {num}')
            print(f'ָ☾. suíte -> {hospedagens[num][0]}')
            print(f'ָ☾. 1 data de entrada -> {hospedagens[num][1]}')
            print(f'ָ☾. 2 hora de entrada -> {hospedagens[num][2]}')
            print(f'ָ☾. 3 statos -> {hospedagens[num][3]}')
            print()
            editar_num = int(input('ָ☾. digite o numero do que quer editar : '))
            editar = input('digite a nova informação : ')
            hospedagens[num][editar_num] = editar
            print('suíte editada com suscesso')
            input('pres ENTER para continuar....')
          else :
            print(f'suíte numero {num} não encontrada')
            input('pres ENTER para continuar....')
        elif resp2 == 4 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE CHECK-OUT ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da hospedagem : '))
          if num in hospedagens:
            data = input('digite a data de saida xx/xx/xxxx : ')
            hora = input('digite a hora de saida xx:xx : ')
            print()
            hospedagens[num].append(data)
            hospedagens[num].append(hora)
            print()
            print(f'☾. numero -> {num}')
            print(f'ָ☾. suíte -> {hospedagens[num][0]}')
            print(f'ָ☾. data de entrada -> {hospedagens[num][1]}')
            print(f'ָ☾. hora de entrada -> {hospedagens[num][2]}')
            print(f'ָ☾. statos -> {hospedagens[num][3]}')
            print(f'ָ☾. data de saida -> {hospedagens[num][4]}')
            print(f'ָ☾. hora de saida -> {hospedagens[num][5]}')
            print(f'ָ☾. total de consumo -> {hospedagens[num][3]}')
            print(f'ָ☾. valor total -> a definir')
            print()
            suite = hospedagens[num][0]
            resp4 = input('dejeja fechar essa hospedagem ? [S/N] ')
            suites[suite][2] = 'livre'
            hospedagens[num][3] = 'fechado'
            print('check-out realizado com suscesso !')
          else:
            print(f'hospedagem numero {num} não encontrada')
            input('pres ENTER para continuar....')

        elif resp2 == 5 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EXCLUIR HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da hospedagem que deseja excluir : '))
          print()
          if num in hospedagens :
            print(hospedagens[num])
            resp = input('deseja mesmo deletar essa hospedagens ? [S/N] ')
            if hospedagens[num][3] == 'em aberto':
              if resp in 'sS' :
                del(hospedagens[num])
                suite = hospedagens[num][0]
                suites[suite][2] = 'livre'
                print('hospedagem excluida com suscesso')
                input('pres ENTER para continuar....')
              else :
                print('operação canselada')
                input('pres ENTER para continuar....')
            else: 
              print(f'hospedagem ainda em aberto, finalize a hospedagem e tente novamente')
              input('pres ENTER para continuar....')
          else : 
            print(f'hospedagem numero {num} não encontrada')
            input('pres ENTER para continuar....')
                    
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
        print('5 𓊯    resistrar pedido     𓊯')
        print('6 𓊯    consultar consumo    𓊯')
        print('0 𓊯         voltar          𓊯')
        print()
        resp2 = int(input('🤍ྀི  digite o numero da operação : '))
        os.system('cls')
        os.system('clear')
        if resp2 == 1 :
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
          print()
          num = len(produtos)+1
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
            for i in range(1,(len(produtos)+1)):
              print()
              print('☕︎ 𓎩 ‧₊˚'*15)
              print()
              print(f'produto numero -> {i}')
              print()
              print(f'𓊯 nome -> {produtos[i][0]}')
              print(f'𓊯 estoque -> {produtos[i][1]}')
              print(f'𓊯 preço -> R$ {produtos[i][2]}')
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
        elif resp2 == 5 :
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PEDIDO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
          print()
          num = len(consumo)+1
          hospedagem = int(input('𓊯 digite o numero da hospedagem : '))
          produto = int(input('𓊯 digite o numero do produto : '))
          quantidade = int(input('𓊯 digite a quantidade que deseja : '))
          consumo[num] = [hospedagem,produto,quantidade]
          print('pedido cadastrado com sucesso')
          input('tecle o ENTER para continuar.....')
        
        elif resp2 == 6 :
          print()
          print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
          print()
          print('1 ָ☾. listar todas')
          print('2 ָ☾. buscar por numero')
          print()
          resp3 = int(input('🤍ྀི  digite o numero da operação : '))
          if resp3 == 1 :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            for i in range(1,(len(consumo)+1)):
              print()
              print('☕︎ 𓎩 ‧₊˚'*15)
              print()
              print(f'pedido numero -> {i}')
              print()
              print(f'𓊯 hospedagem -> {consumo[i][0]}')
              print(f'𓊯 produto -> {consumo[i][1]}')
              print(f'𓊯 quantidade -> {consumo[i][2]}')
            print()
            print('☕︎ 𓎩 ‧₊˚'*15)
            print()
            input('tecle ENTER para continuar.....')
          
          else :
            print()
            print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
            print()
            num = int(input('digite o numero do pedido que deseja consultar : '))
            if num in produtos :
              print()
              print(f'pedido numero -> {num}')
              print()
              print(f'𓊯 hospedagem -> {consumo[num][0]}')
              print(f'𓊯 produto -> {consumo[num][1]}')
              print(f'𓊯 quantidade -> {consumo[num][2]}')
              print()
              input('tecle ENTER para continuar.....')
            else : 
              print(f'pedido numero {num} não encontrado')
              input('tecle ENTER para continuar.....')
      

      
    elif resp == 4 :
      print()
      print('-ˋˏ✄┈┈┈┈ MÓDULO DE RELATORIO -ˋˏ✄┈┈┈┈')
      print()
      print('1 ╰┈➤ relatorio de suites ocupadas')
      print('2 ╰┈➤ relatorio de hospedagens  ')
      print('3 ╰┈➤ relatorio de consumo ')
      print('4 ╰┈➤ relatorio de faturamento ')
      print('5 ╰┈➤ relatorio de estoque ')
      print('0 ╰┈➤ voltar ')
      print()
      resp2 = int(input('🤍ྀི digite o numero da operação : '))

    elif resp == 5 :
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