from verifica import verifica_cpf, verifica_float, verifica_int

def menu_pedidos() : 
        print()
        print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅ MÓDULO DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
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
        return resp2

def cadastrar_pedidos(pedidos,hospedagens,produtos):
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
        if produto not in produtos :
            print()
            print('! PRODUTO NAO ENCONTRADO !')
            input('tecle ENTER para continuar....')
        else:
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

def consultar_pedidos():
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
        return resp3

def listagem_produtos(pedidos,hospedagens,produtos): 
        print()
        print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PEDIDOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
        print()
        for chave, dados in pedidos.items() :
                if dados['ativo'] :
                        print()
                        print(f'||| PEDIDO {chave:^5} |  HOSPEDAGEM > {dados['hospedagem']:^10}  |  PRODUTO  >  R${produtos[dados['produto']]['produto']:^10} |  QUANTIDADE  > {dados['quantidade']:^10} |  STATUS  > {dados['status']:^10} |||')
        print()
        print()
        input('tecle ENTER para continuar.....')





