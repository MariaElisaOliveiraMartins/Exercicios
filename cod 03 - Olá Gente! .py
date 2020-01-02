''' Exemplo de função c/ multiplos parametros'''

def ola_gente(param01,param02,param03='!'):
    return f'===> {param01} Minha {param02}{param03} <===\n'

print('\nExemplo de função c/ vários parametros\n')
print(ola_gente('Olá', 'Gente'))
print(type(ola_gente))