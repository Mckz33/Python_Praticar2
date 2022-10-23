# Secão 2 Video 38
# explicaçao no video 39


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')
    if chances < 0:
        print('Voce perdeu! ')
        break

    if len(letra) > 1:  # len = conta a quantidade de caractere digitada pelo usuario.
        print('Digite apenas uma letra. ')
        continue  # pular para a proxima execução do laço

        # salvar cada letra que o usuario digitou

    digitadas.append(letra) #

    if letra in secreto: # Se a letra fizer parte da variavel string.
        print('\nA letra {} existe na palavra secreta. '.format(letra))
    else:
        print('\nA letra {} não existe'.format(letra))
        digitadas.pop() # O ultimo elemento add será removido da lista.

    secretoTemporario = ''

    for letraSecreta in secreto: # Se a letraSecreta esta dentro da var digitada, o que eu quero colocar dentro do meu secreto
        if letraSecreta in digitadas:
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*'

    if secretoTemporario == secreto:
        print('\nVOCÊ GANHOU!!! ')
        break
    else:
        print('\nA palavra secreta está assim: {}'.format(secretoTemporario))

    if letra not in secreto:
        chances -= 1

    print('Voce ainda tem {} chances'.format(chances))