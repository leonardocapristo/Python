#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
x = float(input('Digite o preço: '))
desconto = x * 0.05 
np = x - desconto
print(np)