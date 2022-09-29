def caixa_eletronico(quantia):
    if quantia >= 10 or quantia <= 600:
        cem = int(quantia/100)
        quantia = quantia%100

        cinquenta = int(quantia/50)
        quantia = quantia%50

        vinte = int(quantia/20)
        quantia = quantia%20

        dez = int(quantia/10)
        quantia = quantia%10

        cinco = int(quantia/5)
        quantia = quantia%5

        um = quantia

        if cem != 0:
            print(f'{cem} nota(s) de cem')
        if cinquenta != 0:
         print(f'{cinquenta} nota(s) de cinquenta')
        if vinte != 0:
         print(f'{vinte} nota(s) de vinte')
        if dez != 0:
         print(f'{dez} nota(s) de dez')
        if cinco != 0:
         print(f'{cinco} nota(s) de cinco')
        if um != 0:
         print(f'{um} nota(s) de um')
    else:
        print('A quantia deve ser de pelo menos 10 reais e de no maximo 600 reais.')

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

def soma_dos_quadrados(l):
    #for loop normal
    acumulador = 0
    for item in l:
        quadrado = item * item
        acumulador += quadrado
    print(f' <for loop> A soma dos quadrados dos elementos da estrutura é {acumulador}')

    #list comprehension
    a = sum([item * item for item in l])
    print(f'<list comprehension> A soma dos quadrados dos elementos da estrutura é {a}')

    #map
    b = sum(map(lambda n : n*n, l))
    print(f'<lambda + map> A soma dos quadrados dos elementos da estrutura é {b}')

def array_intercalado(l1, l2):
    l3 = []
    for c in range(len(l1)):
        l3.append(l1[c])
        l3.append(l2[c])
    
    print(l3)