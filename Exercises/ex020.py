#* O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a = input("Name of the first student: ")
b = input("Name of the second student: ")
c = input("Name of the third student: ")
d = input("Name of the fourth student: ")

list = [a, b, c, d]

print(random.sample(list, 4))