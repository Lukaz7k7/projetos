from verifica import verifica_int, verifica_float

def menu_suites():
    print()
    print('✩₊˚.⋆☾⋆⁺₊✧ MÓDUULO DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
    print()
    print('1 ☪︎ cadastrar suítes ☪︎')
    print('2 ☪︎ consultar suítes ☪︎')
    print('3 ☪︎  editar suítes   ☪︎')
    print('4 ☪︎  excluir suíte   ☪︎')
    print('0 ☪︎     voltar       ☪︎')
    print()

def cadastrar_suites(suites):
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
    valor_s = input('☪ informe o valor por hora : R$ ')
    while not verifica_float(valor_s):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              valor_s = input('🤍ྀི  digite um valor valido : ')
    valor_s = float(valor_s)
    print()
    suites[numero_s] = {
    'tipo' : tipo_s, 
    'valor': valor_s,
    'status': 'livre',
    'ativo': True
    }
    print('suíte cadastrada com suscesso !')
    input('pres ENTER para continuar...')

def consulta_suites():
    print()
    print('✩₊˚.⋆☾⋆⁺₊✧ CONSULTAR SUÍTE ✩₊˚.⋆☾⋆⁺₊✧')
    print()
    print('1 ☪︎ listar todas')
    print('2 ☪︎ buscar por numero')
    print()
    resp3 = input('🤍ྀི  digite o numero da operação : ')
    while not verifica_int(resp3):
        print()
        print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
        print()
        resp3 = input('🤍ྀི   digite sua resposta : ')
    resp3 = int(resp3)
    return resp3 

def listagem_suites(suites):
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

def pesquisa_suites(suites):
    print()
    print('✩₊˚.⋆☾⋆⁺₊✧ PESQUISA DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
    print()
    num = input('digite o numero da suíte que deseja consultar : ')
    while not verifica_int(num):
        print()
        print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
        print()
        num = input('🤍ྀི  digite o numero da suíte que deseja consultar : ')
    num = int(num)
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

def edição_suites(suites):
    print()
    print('✩₊˚.⋆☾⋆⁺₊✧ EDIÇÃO DE SUÍTES ✩₊˚.⋆☾⋆⁺₊✧')
    print()
    num = input('digite o numero da suíte que deseja editar : ')
    while not verifica_int(num):
        print()
        print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
        print()
        num = input('🤍ྀི  digite o numero da suíte que deseja editar : ')
    num = int(num)
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

            valor_s = input('☪ valor por hora : R$ ')
            while not verifica_float(valor_s):
              print()
              print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
              print()
              valor_s = input('🤍ྀི  digite um valor valido : ')
            valor_s = float(valor_s)
            suites[num] = {
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


