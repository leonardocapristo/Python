'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear 
a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
mostre a ordem sorteada.'''

from random import shuffle
a1 = input('digite o primeiro: ')
a2 = input('digite o seungo : ')
a3 = input('digite o terceiro: ')
a4 = input('digite o quarto: ')
lista = [a1 , a2, a3, a4]
shuffle(lista)
print ('a ordem é: ')
print (lista)

#OU

'''import random
a1 = input('digite o primeiro: ')
a2 = input('digite o seungo : ')
a3 = input('digite o terceiro: ')
a4 = input('digite o quarto: ')
lista = [a1 , a2, a3, a4]
random.shuffle(lista)
print ('a ordem é: ')
print (lista)'''
