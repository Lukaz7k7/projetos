import os , time

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
          input('☪ número da suíte : ')
          input('☪ tipo [1-simples / 2-luxo / 3-premium] : ')
          input('☪ valor por hora : R$ ')
          print()
          print('suíte cadastrada com suscesso !')
          print('ATENÇÃO ! isso é apenas uma simulação')
          time.sleep(2)

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
            print('☪ numero -> 123')
            print('☪ tipo -> simples')
            print('☪ valor por hora -> R$35')
            print('☪ status -> livre')
            print()
            print('☪-☪'*25)
            print()
            print('☪ numero -> 69')
            print('☪ tipo -> premium')
            print('☪ valor por hora -> R$69')
            print('☪ status -> ocupada')
            print()
            print('☪-☪'*25)
            print()
            print('ATENÇÃO ! isso é apenas uma simulação')
            input('tecle ENTER para continuar ....')
          else : 
            print()
            print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
            print()
            num = int(input('digite o numero da suíte que deseja consultar : '))
            print()
            print(f'☪ numero -> {num}')
            print('☪ tipo -> simples')
            print('☪ valor por hora -> R$35')
            print('☪ status -> livre')
            print()
            print('ATENÇÃO ! isso é apenas uma simulação')
            input('tecle ENTER para continuar .....')
        elif resp2 == 3  :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EDIÇÃO DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da suíte que deseja editar : '))
          input('☪ novo número da suíte : ')
          input('☪ tipo [1-simples / 2-luxo / 3-premium] : ')
          input('☪ valor por hora : R$ ')
          print('suíte editada com suscesso')
          print('ATENÇÃO ! isso é apenas uma simulação')
          time.sleep(2)
        elif resp2 == 4 :
          print()
          print('✩₊˚.⋆☾⋆⁺₊✧ EXCLUIR SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
          print()
          num = int(input('digite o numero da suíte que deseja excluir : '))
          print()
          print(f'☪ numero -> {num}')
          print('☪ tipo -> simples')
          print('☪ valor por hora -> R$35')
          print('☪ status -> livre')
          print()
          print('suíte excluida com suscesso')
          print('ATENÇÃO ! isso é apenas uma simulação')
          time.sleep(2)

    elif resp == 2 :
      print()
      print('✩₊˚.⋆☾⋆⁺₊✧ MÓDULO DE HOSPEDAGEM ✩₊˚.⋆☾⋆⁺₊✧')
      print()
      print('1 ࣪ ִֶָ☾.   Fazer check-in     ࣪ ִֶָ☾.')
      print('2 ࣪ ִֶָ☾. consultar hospedagem ࣪ ִֶָ☾.')
      print('3 ࣪ ִֶָ☾.   Fazer check-out    ࣪ ִֶָ☾.')
      print('4 ࣪ ִֶָ☾.  excluir hospodegem  ࣪ ִֶָ☾.')
      print('0 ࣪ ִֶָ☾.       voltar         ࣪ ִֶָ☾.')
      
      print()
      resp2 = int(input('🤍ྀི  digite o numero da operação : ')) 

    elif resp == 3 : 
      print()
      print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅ MÓDULO DE PRODUTOS E CONSUMO ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
      print()
      print('1 𓊯   cadastrar produstos   𓊯')
      print('2 𓊯      ver produtos       𓊯')
      print('3 𓊯     editar produto      𓊯')
      print('4 𓊯     exclir produto      𓊯')
      print('5 𓊯    resistrar pedido     𓊯')
      print('6 𓊯    consultar consumo    𓊯')
      print('0 𓊯         voltar          𓊯')
      print()
      resp2 = int(input('🤍ྀི  digite o numero da operação : '))
      
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