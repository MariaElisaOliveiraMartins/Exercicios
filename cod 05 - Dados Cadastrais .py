""" Exemplo função com passagem parametros de estrutura complexa, isso é, registros"""

def dados_cadastrais(*parametros):
    print(type(parametros))
    for ptr in parametros:
        print(ptr)


print('\n ---> INICIO <---- \n')
dados_cadastrais('Maria Elisa','Rua Elso Previtale, 645 casa 242','CEP: 13272-300 - Valinhos / SP')
dados_cadastrais('CPF: 043.674.818-59','RG: 13.629.120','Cel: +55 (19) 98119-6965')
print('\n ---> FIM <--- \n')

