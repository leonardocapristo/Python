'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

a1 = input('digite o nome do primeiro aluno')
a2 = input('digite o segundo: ')
a3 = input('digite o terceiro: ')
a4 = input('digite o quarto : ')
lista = a1, a2, a3, a4
escolhido = random.choice(lista)
print('o aluno escolhido foi {} '.format(escolhido))