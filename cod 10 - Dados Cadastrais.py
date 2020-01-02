"""

Exemplo função com passagem parametros de estrutura complexa e manipulação de indices

Obs: nesse exemplo, a função efetua um merge entre duas tuplas

"""

def dados_cadastrais(tit,dad):
    for idx in zip(tit,dad):
        print(idx)



print('\n ---> INICIO <---- \n')
titulos = ('Nome: ', 'Endereço: ', 'CEP: ', 'Cidade: ', 'UF: ', 'CPF: ', 'RG: ', 'Cel :')
dados = ('Maria Elisa', 'Rua Elso Previtale, 645 casa 242', '13272-300', 'Valinhos', 'SP', '043.674.818-59', '13.629.120','+55 (19) 98119-6965')
dados_cadastrais(titulos,dados)
print('\n ---> FIM <--- \n')