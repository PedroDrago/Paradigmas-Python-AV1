#1.
def peso_ideal(h):
    peso_ideal_masc = (72.7 * h) - 58
    peso_ideal_fem = (62.1 * h) - 44.7

    print(f'Caso homem, o peso ideal para a altura {h} é {peso_ideal_masc:.2f}')
    print(f'Caso mulher, o peso ideal para a altura {h} é {peso_ideal_fem:.2f}')

def valor_multa(peso):
    if peso < 50:
        print('Não há excesso, logo, não há multa para caulcular.')
    else:
        excesso = peso - 50
        #a transformacao em int nesse passo faz com que caso o peso seja inserido com casas decimais, o calculo so sera feito a cada quilo, e nao em cima das casa decimais
        #se deixasse sem, o valor de 60.0 kg e 60.2 kg seria diferente, e nao deveria, ja que so se paga a cada kilo a mais
        multa = int(excesso) * 4.00
        print(f'O valor da multa para um excesso de {excesso:.1f} Kg é de R${multa}')

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

salario(10, 10)