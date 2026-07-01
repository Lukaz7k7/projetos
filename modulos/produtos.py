from verifica import verifica_cpf, verifica_float, verifica_int

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

def cadastrar_produtos(produtos):
        print()
        print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CADASTRO DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
        print()
        num = max(produtos.keys()) + 1
        print(f'NUMERO DO PRODUTO -> {num}')
        print()
        produto = input('𓊯 digite o nome do produto para cadastrar : ')
        estoque = input('𓊯 digite a quantidade que tem no estoque : ')
        while not verifica_int(estoque):
            print()
            print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
            print()
            estoque = input('🤍ྀི  digite a quantidade que tem no estoque : ')
        estoque = int(estoque)
        valor = input('𓊯 digite o preço do produto : ')
        while not verifica_float(valor):
            print()
            print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
            print()
            valor = input('🤍ྀི  digite o preço do produto : ')
        valor = float(valor)
        produtos[num] = {
        'produto' : produto, 
        'estoque' : estoque,
        'valor' : valor,
        'ativo' : True
        }
        print('produto cadastrado com sucesso')
        input('tecle o ENTER para continuar.....')

def consultar_produtos():
    print()
    print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  CONSULTA DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
    print()
    print('1 ָ☾. listar todas')
    print('2 ָ☾. buscar por numero')
    print()
    resp3 = input('🤍ྀི  digite o numero da operação : ')
    while not verifica_int(resp3):
        print()
        print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
        print()
        resp3 = input('🤍ྀི  digite o numero da operação : ')
    resp3 = int(resp3)
    return resp3

def listagem_produtos(produtos):
    print()
    print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  LISTAGEM DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
    print()
    for chave, dados in produtos.items() :
        if dados['ativo']:
            print()
            print('☕︎ 𓎩 ‧₊˚'*15)
            print()
            print(f'|||   PRODUTO {chave:^5} |  NOME > {dados['produto']:^30}  |  PREÇO  >  R${dados['valor']:^10}  |  ESTOQUE  > {dados['estoque']:^10} |||')
    print()
    print('☕︎ 𓎩 ‧₊˚'*15)
    print()
    input('tecle ENTER para continuar.....')

def pesquisa_produtos(produtos):
    print()
    print('‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅  PESQUISA DE PRODUTOS ‧₊˚ ⋅ ☕︎ 𓎩 ‧₊˚ ⋅')
    print()
    num = input('digite o numero do produto que deseja consultar : ')
    while not verifica_int(num):
        print()
        print('! RESPOSTA INVALIDA, DIGITE UMA RESPOSTA VALIDA !')
        print()
        num = input('🤍ྀི  digite o numero do produto que deseja consultar : ')
    num = int(num)
    if num in produtos and produtos[num]['ativo'] :
        print()
        print(f'|||   PRODUTO {num:^5} |  NOME > {produtos[num]['produto']:^30}  |  PREÇO  >  R${produtos[num]['valor']:^10}  |  ESTOQUE  > {produtos[num]['estoque']:^10} |||')
        print()
        input('tecle ENTER para continuar.....')
    else : 
        print(f'produto numero {num} não encontrado')
        input('tecle ENTER para continuar.....')
