from verifica import verifica_cpf, verifica_int

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