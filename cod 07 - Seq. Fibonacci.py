"""

    Esse programa calcula N elementos da sequencia de Fibonacci dentro de um intervalo
    definido e precedido do seu indice de ordenação.

"""

def sequencia_fibonacci (inic,fim):

    ant = 1
    prox = 1
    print('===> Sequencia de Fibonacci entre ', inic, ' e ', fim, ' <===\n')

    for cont in range(1,fim,1):
        if inic <= prox <= fim:
            print(cont,'º - ', prox)
        aux = ant
        ant = prox
        prox = ant + aux


sequencia_fibonacci(8,150)



