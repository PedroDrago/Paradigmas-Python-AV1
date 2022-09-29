import math
#1.
def peso_ideal(h):
    peso_ideal_masc = (72.7 * h) - 58
    peso_ideal_fem = (62.1 * h) - 44.7

    print(f'Caso homem, o peso ideal para a altura {h} é {peso_ideal_masc:.2f}')
    print(f'Caso mulher, o peso ideal para a altura {h} é {peso_ideal_fem:.2f}')
#2
def valor_multa(peso):
    if peso < 50:
        print('Não há excesso, logo, não há multa para caulcular.')
    else:
        excesso = peso - 50
        #a transformacao em int nesse passo faz com que caso o peso seja inserido com casas decimais, o calculo so sera feito a cada quilo, e nao em cima das casa decimais
        #se deixasse sem, o valor de 60.0 kg e 60.2 kg seria diferente, e nao deveria, ja que so se paga a cada kilo a mais
        multa = int(excesso) * 4.00
        print(f'O valor da multa para um excesso de {excesso:.1f} Kg é de R${multa}')
#3
def salario(salario_por_hora, horas_trabalhadas):
    salario_bruto = salario_por_hora * horas_trabalhadas
    imposto_de_renda = (salario_bruto * 0.11)
    inss = (salario_bruto * 0.08)
    sindicato =(salario_bruto * 0.05)
    descontos = imposto_de_renda + inss + sindicato
    salario_liquido = salario_bruto - descontos
    print(f'Salário bruto: + R$ {salario_bruto}')
    print(f'Imposto de renda: - R$ {imposto_de_renda}')
    print(f'INSS: - R$ {inss}')
    print(f'Sindicato: - R$ {sindicato}')
    print(f'Salário liquido = R$ {salario_liquido}')
#4
def tinta_latas(area):
    quantidade_de_litros = area / 3
    quantidade_de_latas = math.ceil(quantidade_de_litros / 18)
    preco = quantidade_de_latas * 80.00

    print(f'Com uma área de {area} metros quadrados, você deve comprar {quantidade_de_latas} latas de tinta, que custará R$ {preco:.2f}')

#5
def tinta_galoes_latas(area):
    litros_necessarios = area/6
    apenas_latas = math.ceil(litros_necessarios/18)
    apenas_galoes = math.ceil(litros_necessarios/3.6)

    latas = int(litros_necessarios/18)
    litros_necessarios = litros_necessarios%18
    galoes = math.ceil(litros_necessarios/3.6)

    preco_misto = (latas * 80.0) + (galoes * 25.0)

    print(f'Em caso de compra mista compre: {latas} latas e {galoes} galoes, por {preco_misto:.2f}')
    print(f'Em caso de apenas latas compre: {apenas_latas} latas por {(apenas_latas * 80.0):.2f}')
    print(f'Em caso de apenas galoes compre: {apenas_galoes} galoes por {(apenas_galoes * 25.0):.2f}')

#6
def tempo_download(tamanho, velocidade):
    tamanho_megabits = tamanho * 8
    velocidade_segundos = tamanho_megabits / velocidade
    velocidade_minutos = velocidade_segundos / 60

    print(f'O download do arquivo de tamanho {tamanho} MB demorará {velocidade_minutos:.2f} minutos.')

