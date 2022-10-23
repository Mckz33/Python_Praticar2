'''1- Crie uma funçao que exiibe uma saudaçao com os parametros saudaçao e nome.'''

'''
def saudacao (saudacao, nome):
    print(f'{saudacao} {nome}')
saudacao('Olá', 'iza')
saudacao('oi', 'isabela')
saudacao('hey', 'cristineide')
'''

'''2- Crie uma funçao que recebe 3 numeros como parammetros  e exiba a soma entre eles.'''

'''
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(2, 1, 3)
soma(1, 1, 1)
soma(2, 1, 1)
'''
'''3- cre uma funçao que receba 2 numeros. o primeiro é um valor e o segundo um percentual (ex. 10%).
retorne (return) o valor do primero numero somado do aumento do percentual do mesmo.'''

'''
def aumentoPercentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumentoPercentual(50, 10)
print(ap)
ap = aumentoPercentual(100, 10)
print(ap)
ap = aumentoPercentual(10, 10)
print(ap)
ap = aumentoPercentual(13, 100)
print(ap)
'''

'''4- fizz buzz - se o parametro da funçao for divisivel por 3, retorne fizz, se o parametro da funçao
for divisivel por 5, retorne buzz. se o parametro da funçao for divisivel por 5 e por 3, retorne fizzBuzz, 
caso contrario, retorne o numero enviado.'''

'''
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz {n} é divisivel por 3 e 5'
    if n % 5 == 0:
        return f'buzz {n} é divisivel por 5 '
    if n % 3 == 0:
        return f'fizz {n} é divisivel por 3'
    return n

print(fb(7))
print(fb(10))
print(fb(15))
print(fb(22))

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
'''

'''
from random import randint
import math

vet1 = [0]*10
vet2 = [0]*10

for i in range(10):
    vet1[i] = randint(10)
    vet2[i] = math.factorial(vet1[i])

print(vet1)
print(vet2)
'''

def potencial(b,e):

    p = 1
    i = 0
    while i < e:
        p *= b
        i += 1
    return p

b = int(input('Base: '))

e = int(input('Expoente: '))

print(f'{b} ^ {e} = {potencial(b, e)}')
