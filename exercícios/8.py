#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite a medida em metro: '))
cm = medida * 100
mm = cm * 10
print('O valor de {} em metro convertido para cm é {} e em mm é {}'.format(medida, cm, mm))