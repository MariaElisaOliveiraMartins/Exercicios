"""

Exemplo função com passagem parametros de estrutura complexa e manipulação de indices

Obs: nesse exemplo, a função efetua um merge tratando duas tuplas como vetores,
incrementando os indices e gerando um dicionário (hashing) de dados a partir das tuplas.

"""

def dados_cadastrais(tit,dad):
    print(type(tit),tit)
    print(type(dad),dad)
    cad = {}
    for idx_1 in range(0,len(tit),1):
        idx_2 = idx_1
        cad[tit[idx_1]] = dad[idx_2]
    return(cad)


print('\n ---> INICIO <---- \n')

titulos = ('Nome: ', 'Endereço: ', 'CEP: ', 'Cidade: ', 'UF: ', 'CPF: ', 'RG: ', 'Cel :')
dados = ('Maria Elisa', 'Rua Elso Previtale, 645 casa 242', '13272-300', 'Valinhos', 'SP', '043.674.818-59', '13.629.120','+55 (19) 98119-6965')

cadastro = dados_cadastrais(titulos,dados)

''' Exibe o returno da função'''
print('\n',type(cadastro),cadastro,'\n')

''' Exibe todos os items retornados '''
for t,d in cadastro.items():
    print(t,d)

''' Seleciona e exibe dados conforme argumento de pesquisa '''
print('O número do CEP é ',cadastro.get('CEP: '))
print('A sigla do estado é ',cadastro.get('UF: '))
print('\n')

''' Elimina os dois items pesquisados '''
cadastro.pop('CEP: ')
del cadastro['UF: ']
print(cadastro)

print('\n ---> FIM <--- \n')