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

def alturas_e_idades():
    array_altura = []
    array_idade = []
    for c in range(5):
        idade = int(input(f'Digite a idade da {c+1} pessoa: '))
        altura = float(input(f'Digite a altura da {c+1} pessoa: '))
        array_idade.append(idade)
        array_altura.append(altura)
    array_altura.reverse()
    array_idade.reverse()
    for c in range(5):
        print(f'idade da pessoa {5-c}: {array_idade[c]}')
        print(f'altura da pessoa {5-c}: {array_altura[c]}')

alturas_e_idades()