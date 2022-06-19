#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Digite a altura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = altura * comprimento
print('A área é de:', area, 'm²')
tinta = area / 2
print ('Para pintar essa parede você irá precisar de ',tinta, 'litros de tinta')
