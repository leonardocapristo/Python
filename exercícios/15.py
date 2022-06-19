#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
#a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.




dias = float(input('quantos dias foram alugados ?: '))
tarifa1 = dias * 60
t2 = dias * 0.15
preco = tarifa1 + t2
print(tarifa1 + t2)