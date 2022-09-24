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

valor_multa(70)