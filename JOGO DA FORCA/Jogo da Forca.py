secreto = str(input('Digite uma palavra: '))
secretoTemporario = ''

digitadas = ['m']

for letraSecreta in secreto:
    print('iteraçao para letra {}'.format(letraSecreta))

    if letraSecreta in digitadas:
        print('EBAAAAAAAAAAAA ACHOU!: {}'.format(letraSecreta))
        secretoTemporario += letraSecreta

print(secretoTemporario)