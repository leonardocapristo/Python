#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro do número {} é {} , o triplo é {}\ne sua raíz é {}' .format(n, dobro, triplo, raiz))