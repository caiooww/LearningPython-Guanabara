#* Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random

a = input("Name of the first student: ")
b = input("Name of the second student: ")
c = input("Name of the third student: ")
d = input("Name of the fourth student: ")

list = [a, b, c, d]

print(random.choice(list))