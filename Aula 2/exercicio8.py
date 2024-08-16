#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = int(input('quanto você ganha por hora? '))
numero_de_hora = int(input('Qual a quantidade de horas que você trabalha ? '))
mes = 30


total = (ganho_por_hora * numero_de_hora * mes )

print('o seu salario total é ? ', total)
