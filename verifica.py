def verifica_cpf(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    if len(cpf) != 11:
        return False
    for caractere in cpf:
        if caractere < '0' or caractere > '9':
            return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    d1 = 11 - (soma % 11)
    if d1 >= 10:
        d1 = 0
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    d2 = 11 - (soma % 11)
    if d2 >= 10:
        d2 = 0
    if d1 == int(cpf[9]) and d2 == int(cpf[10]):
        return True
    return False

def verifica_int(x):
    try:
        int(x)
        return True

    except :
        return False
        

def verifica_float(x):
    try:
        float(x)
        return True

    except :
        return False