#1.
def peso_ideal(h):
    peso_ideal_masc = (72.7 * h) - 58
    peso_ideal_fem = (62.1 * h) - 44.7

    print(f'Caso homem, o peso ideal para a altura {h} é {peso_ideal_masc:.2f}')
    print(f'Caso mulher, o peso ideal para a altura {h} é {peso_ideal_fem:.2f}')