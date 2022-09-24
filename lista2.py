def caixa_eletronico():
    return 0

def par_ou_impar(n):
    if n%2 == 0:
        print(f'{n} é um numero par')
    else:
        print(f'{n} é um numero ímpar')

def inteiro_ou_decimal(n):
    if type(n) == int:
        print(f'{n} é um numero inteiro')
    elif type(n) == float:
        print(f'{n} é um numero decimal')
    else:
        print(f'{n} não é um numero')

