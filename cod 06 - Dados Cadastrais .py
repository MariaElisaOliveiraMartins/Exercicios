"""

 Exemplo função com passagem parametros de estrutura complexa e manipulação de indices

 Obs: nesse exemplo, a função trata a tupla como um vetor de strings, exibindo os dados
 em ordem descrecente, isso é, decrementando o indice.

"""


def dados_cadastrais(*parametros):
    for idx in range(len(parametros)-1, -1, -1):
        print(idx, ' - ', parametros[idx])
        
print('\n ---> INICIO <---- \n')

dados_cadastrais('Maria Elisa', 'Rua Elso Previtale, 645 casa 242', 'CEP: 13272-300 - Valinhos / SP')

dados_cadastrais('CPF: 043.674.818-59', 'RG: 13.629.120', 'Cel: +55 (19) 98119-6965')

print('\n ---> FIM <--- \n')
