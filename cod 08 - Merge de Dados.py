"""

    Esse programa efetua o merge de duas listas de números
    gerando uma única sequencia numérica.

"""

def sequencia_numerica (lista_1,lista_2):

    print('\n===> Sequencia <===')

    for lista_1, lista_2 in zip(lista_1,lista_2):
        if lista_1 <= lista_2:
            print(lista_1,lista_2,'\n')
        else:
            print(lista_2,lista_1,'\n')
    

print('exemplo:')

sequencia_numerica([1,3,5,7,9,11,13],[0,2,4,6,8,10,12])
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
sequencia_numerica(l1,l2)
