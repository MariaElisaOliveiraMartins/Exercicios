"""

Exemplo função com passagem parametros de estrutura complexa e manipulação de indices

Obs: nesse exemplo, a função trata a tupla como um vetor de strings, exibindo os dados
em ordem descrecente, isso é, decrementando o indice.

"""


def somatorio(*numeros):
    soma = 0
    for idx in range(0, len(numeros), 1):
        soma += numeros[idx]
    return (soma)

print('\n ---> INICIO <---- \n')

print(somatorio(1, 2, 3, 4, 5,))
print(somatorio(10, 20, 30, 40, 50, 60, 70, 80))

print('\n ---> FIM <--- \n')
