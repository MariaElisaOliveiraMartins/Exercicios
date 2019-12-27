"""

    Esse programa calcula e exibe os elementos da sequencia de Fibonacci
    em um intervalo definido por dois números naturais onde cada elemento é
    precedido pelo seu respectivo índice na sequencia.

"""

def sequencia_fibonacci (inic, fim):
    i = j = 1
    prox = 0
    if inic == 1:
        print('1 -> ',i)
        print('2 -> ',j)
    cont = 3
    while prox < fim:
        prox = i + j
        if inic <= prox <= fim:
            print(cont, ' -> ', prox)
        i = j
        j = prox
        cont += 1

print(sequencia_fibonacci(10,300))













