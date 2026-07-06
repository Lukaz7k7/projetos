import os , time 
from datetime import datetime
from verifica import verifica_cpf, verifica_int, verifica_float
from armazenamento import recupera_suites , salva_suites , recupera_hospedagens, salva_hospedagens, recupera_produtos , salva_produtos, recupera_pedidos, salva_pedidos
from modulos.suites import listagem_suites, cadastrar_suites , menu_suites, pesquisa_suites, consulta_suites , edição_suites , exclui_suites
from modulos.hospedagens import menu_hospedagens,cadastrar_hospedagens,consultar_hospedagens, listagem_hospedagens, pesquisa_hospedagens, finalizar_hospedagens
from modulos.pedidos import menu_pedidos, cadastrar_pedidos, consultar_pedidos, listagem_pedidos, pesquisa_pedidos, pesquisa_pedidos_hospedagem,cancelar_pedidos
from modulos.produtos import menu_produtos,cadastrar_produtos, consultar_produtos, listagem_produtos,pesquisa_produtos,editar_produtos,exclui_produtos 
from modulos.relatorio import menu_relatorio, relatorio_suites, relatorio_produtos, relatorio_hospedagens, relatorio_pedidos

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
          salva_suites(suites)

        elif resp2 == 2 :
          
          resp3 = consulta_suites()

          if resp3 == 1 :

            listagem_suites(suites)
            
          else : 
          
            pesquisa_suites(suites)

        elif resp2 == 3  :

          edição_suites(suites)
          salva_suites(suites)
                
        elif resp2 == 4 :

          exclui_suites(suites)
          salva_suites(suites)

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
          
          cadastrar_hospedagens(hospedagens,suites)
          salva_hospedagens(hospedagens)


        elif resp2 == 2 :

          resp3 = consultar_hospedagens()

          if resp3 == 1 :
            
            listagem_hospedagens(hospedagens)

          else : 
            
            pesquisa_hospedagens(hospedagens)
      
        elif resp2 == 3 :

          finalizar_hospedagens(hospedagens,suites,pedidos,produtos)
          salva_hospedagens(hospedagens)


    # módulo de produtos         
                    
    elif resp == 3 : 
      resp2 = ''
      while resp2 != 0 :
        os.system('cls')
        os.system('clear')

        resp2 = menu_produtos()

        os.system('cls')
        os.system('clear')

        if resp2 == 1 :

          cadastrar_produtos(produtos)
          salva_produtos(produtos)

        elif resp2 == 2 :

          resp3 = consultar_produtos()

          if resp3 == 1 :
            
            listagem_produtos(produtos)
          
          else :

            pesquisa_produtos(produtos)

        elif resp2 == 3 :

            editar_produtos(produtos)
            salva_produtos(produtos)

        elif resp2 == 4 :
            exclui_produtos(produtos)
            salva_produtos(produtos)

    #módulo de pedidos         
        
    elif resp == 4 : 
        resp2 = ''
        while resp2 != 0 :
          os.system('cls')
          os.system('clear')

          resp2 = menu_pedidos()

          os.system('cls')
          os.system('clear')

          if resp2 == 1 :

            cadastrar_pedidos(pedidos,hospedagens,produtos)
            salva_pedidos(pedidos)
        
          elif resp2 == 2 :
            
            resp3 = consultar_pedidos()

            if resp3 == 1 :

              listagem_pedidos(pedidos,hospedagens,produtos)
            
            elif resp3 == 2 :
              
              pesquisa_pedidos_hospedagem(pedidos,hospedagens,produtos)

            elif resp3 == 3:
              
              pesquisa_pedidos(pedidos,hospedagens,produtos)

          elif resp2 == 3 :
            
            cancelar_pedidos(pedidos,hospedagens,produtos)
            salva_pedidos(pedidos)
                    
      
    # módulo de relatorio
      
    elif resp == 5 :
      resp2 = ''
      while resp2 != 0 :
        os.system('cls')
        os.system('clear')

        resp2 = menu_relatorio()
    
        os.system('cls')
        os.system('clear')

        if resp2 == 1 :
          relatorio_suites(suites)
        
        if resp2 == 2 :
          relatorio_hospedagens(hospedagens)

        if resp2 == 3 :
          relatorio_produtos(produtos)
        
        if resp2 == 4 :
          relatorio_pedidos(pedidos,produtos)
        
        

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
