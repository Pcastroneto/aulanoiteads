#1- Escreva um programa que leia 3 notas de um aluno e a média das notas dos exercícios realizados
#por ele. Calcular a média de
#aproveitamento, usando a fórmula:
#MA = (N1 + N2*2 + N3*3 + ME)/7. A
#partir da média, informar o
#conceito de acordo com os itens
#Abaixo:
#maior ou igual a 9
#menor que 4

n1 = float(input("Entre com n1: ")) 
n2 = float(input("Entre com n2: "))
n3 = float(input("Entre com n3: "))
me = float(input("Entre com ME: ")) 

ma = (n1 + n2 * 2 + n3 * 3 + me )/7

if (ma>=9):
    print ("Maior ou igual a 9")
if (ma<4):
    print ("Menor que 4")