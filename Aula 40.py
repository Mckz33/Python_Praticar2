variavel = ['luiz otavio', 'joaozinho', 'maria']

jogalhada = False

for valor in variavel:
    if valor.startswith('m'):
        jogalhada = True

if jogalhada:
    print('Começa')
else:
    print('Nao começa')