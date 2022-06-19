#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário 
#e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário: '))
aumento = salario * 0.15
novosalario = salario + aumento
print (novosalario)