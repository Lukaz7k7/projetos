def menu_produtos():
        
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
        return resp2



