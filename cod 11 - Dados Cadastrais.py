"""

Exemplo função com passagem parametros de estrutura complexa e manipulação de indices

Obs: nesse exemplo, a função efetua um merge tratando duas tuplas como vetores,
incrementando os indices e transformando-as em strings.

"""

def dados_cadastrais(tit,dad):
    print(type(tit), type(dad))
    for idx_1 in range(0,len(tit),1):
        idx_2 = idx_1
        s = tit[idx_1] + dad[idx_2]
        print(type(s),s)



print('\n ---> INICIO <---- \n')

titulos = ('Nome: ', 'Endereço: ', 'CEP: ', 'Cidade: ', 'UF: ', 'CPF: ', 'RG: ', 'Cel :')
dados = ('Maria Elisa', 'Rua Elso Previtale, 645 casa 242', '13272-300', 'Valinhos', 'SP', '043.674.818-59', '13.629.120','+55 (19) 98119-6965')

dados_cadastrais(titulos,dados)

print('\n ---> FIM <--- \n')