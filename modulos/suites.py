

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

