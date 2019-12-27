"""

    Esse programa efetua o merge de duas listas de números gerando uma única sequencia.

"""

def sequencia_numerica (lista_1,lista_2):

    print('\n===> Sequencia <===')

    for lista_1, lista_2 in zip(lista_1,lista_2):
        if lista_1 <= lista_2:
            print(lista_1,lista_2)
        else:
            print(lista_2,lista_1)
    

print('exemplo 01:')
sequencia_numerica([1,3,5,7,9],[0,2,4,6,8])
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
sequencia_numerica(l1,l2)
