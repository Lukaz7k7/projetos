from datetime import datetime

def recupera_suites() :
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
                ativo = dados[4] == "True"
                suites[num] = {
                    'tipo' : tipo, 
                    'valor' : valor,
                    'status' : status,
                    'ativo' : ativo
                            }
        arq_suites.close()

    except : 
        suites = {

                1 : {
                'tipo' : 'premiun',
                'valor' : 69.0,
                'status': 'ocupado',
                'ativo' : True,
                },

                2 : {
                'tipo'  : 'simples',
                'valor' : 24.0,
                'status': 'ocupado',
                'ativo' : True,
                },
                3 : {
                'tipo'  : 'luxo',
                'valor' : 45.50,
                'status': 'livre',
                'ativo' : True,
                },
        }
        arq_suites = open('suites.txt','wt',encoding="utf-8")
        for num, dados in suites.items() :
            arq_suites.write(f'{num},{dados['tipo']},{dados['valor']},{dados['status']},{dados['ativo']}\n')
        arq_suites.close()

    return suites

def salva_suites(suites):
    arq_suites = open('suites.txt','wt',encoding="utf-8")
    for num, dados in suites.items() :
        arq_suites.write(f'{num},{dados['tipo']},{dados['valor']},{dados['status']},{dados['ativo']}\n')
    arq_suites.close()


def recupera_hospedagens() : 
    hospedagens = {}
    try : 
        arq_hospedagens = open('hospedagens.txt','rt',encoding="utf-8")
        for linha in arq_hospedagens :
            linha = linha.strip()
            if linha: 
                dados = linha.split(',')
                num = int(dados[0])
                suite = int(dados[1])
                entrada = datetime.fromisoformat(dados[2])
                cpf = int(dados[3])
                status = dados[4]
                if dados[4] == 'fechado':
                    saida = datetime.fromisoformat(dados[5])
                    valor_t = float(dados[6])
                    hospedagens[num] = {
                    'suite' : suite,
                    'entrada' : entrada,
                    'cpf' : cpf,
                    'status' : status,
                    'saida' : saida,
                    'valor_t' : valor_t,
                        }
                else:
                    hospedagens[num] = {
                    'suite' : suite,
                    'entrada' : entrada,
                    'cpf' : cpf,
                    'status' : status,
                    }
        arq_hospedagens.close()

    except:
        hospedagens = {
            1 : {
            'suite' : 1, 
            'entrada' : datetime(2026, 6, 13, 15, 30, 42) ,
            'cpf' :  10531031403 ,
            'status' :  'em aberto',
            },
            2 : {
            'suite' : 2, 
            'entrada' : datetime(2026, 6, 13, 15, 30, 42) ,
            'cpf' :  10531031403 ,
            'status' :  'em aberto',
                },
            }
        arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
        for num,dados in hospedagens.items() : 
            if dados['status'] == 'fechado' :
                arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']},{dados['saida']},{dados['valor_t']}\n')
            else :
                arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']}\n')
        arq_hospedagens.close()

    return hospedagens

def salva_hospedagens(hospedagens):
    arq_hospedagens = open('hospedagens.txt','wt',encoding="utf-8")
    for num,dados in hospedagens.items() : 
        if dados['status'] == 'fechado' :
            arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']},{dados['saida']},{dados['valor_t']}\n')
        else :
            arq_hospedagens.write(f'{num},{dados['suite']},{dados['entrada']},{dados['cpf']},{dados['status']}\n')
    arq_hospedagens.close()


def recupera_produtos() :
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
                ativo = dados[4]
                produtos[num] = {
                    'produto' : produto, 
                    'estoque' : estoque,
                    'valor' : valor,
                    'ativo' : ativo
                        }
        arq_produtos.close()

    except : 
        produtos = {
            1 : {
                'produto' : 'vinho', 
                'estoque' : 20 ,
                'valor' :  50.0 ,
                'ativo' : True ,
                },
            2 : {
                'produto' : 'lubrificante',
                'estoque' : 15,
                'valor' :  5.5,
                'ativo' : True ,
                },
            3 : {
                'produto' : 'camisinha',
                'estoque' : 15,
                'valor' :  5.5,
                'ativo' : True ,
                },
                }
        arq_produtos = open('produtos.txt','wt',encoding="utf-8")
        for num, dados in produtos.items() :
            arq_produtos.write(f'{num},{dados['produto']},{dados['estoque']},{dados['valor']},{dados['ativo']}\n')
        arq_produtos.close()

def salva_produtos() :
    arq_produtos = open('produtos.txt','wt',encoding="utf-8")
    for num, dados in produtos.items() :
        arq_produtos.write(f'{num},{dados['produto']},{dados['estoque']},{dados['valor']},{dados['ativo']}\n')
    arq_produtos.close()


def recupera_pedidos() : 
    try : 
        arq_pedidos = open('pedidos.txt','rt', encoding="utf-8")
        for linha in arq_pedidos : 
            linha = linha.strip()
            if linha :
                dados = linha.split(',')
                num = int(dados[0])
                hospedagem = int(dados[1])
                produto = int(dados[2])
                quantidade = int(dados[3])
                status = dados[4]
                ativo = dados[5]
                pedidos[num] = {
                    'hospedagem' : hospedagem , 
                    'produto' : produto,
                    'quantidade' : quantidade,
                    'status' : status,
                    'ativo' : ativo,
                    }
        arq_pedidos.close()

    except : 
            pedidos = { 
            1 : {
                'hospedagem' : 1,
                'produto' : 2,
                'quantidade' : 1,
                'status' : 'em aberto',
                'ativo' : True,
                },
            2 : {
                'hospedagem' : 1,
                'produto' : 1,
                'quantidade' : 4,
                'status' : 'em aberto',
                'ativo' : True,
                },
            3 : {
                'hospedagem' : 2,
                'produto' : 1,
                'quantidade' : 4,
                'status' : 'em aberto',
                'ativo' : True,
                },
            4 : {
                'hospedagem' : 2,
                'produto' : 1,
                'quantidade' : 4,
                'status' : 'em aberto',
                'ativo' : True,
                },
            5 : {
                'hospedagem' : 2,
                'produto' : 1,
                'quantidade' : 4,
                'status' : 'em aberto',
                'ativo' : True,
                        },
                    }
            arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
            for num, dados in pedidos.items() :
                arq_pedidos.write(f'{num},{dados['hospedagem']},{dados['produto']},{dados['quantidade']},{dados['status']},{dados['ativo']}\n')
            arq_pedidos.close()

def salva_pedidos() :
    arq_pedidos = open('pedidos.txt','wt',encoding="utf-8")
    for num, dados in pedidos.items() :
        arq_pedidos.write(f'{num},{dados['hospedagem']},{dados['produto']},{dados['quantidade']},{dados['status']},{dados['ativo']}\n')
    arq_pedidos.close()