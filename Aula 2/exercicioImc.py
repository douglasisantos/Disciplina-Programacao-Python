#Faça um programa em Python que receba um nome, uma altura (em cm) e um peso (em kg). Em seguida, calcule e exiba (junto com o nome) o IMC da pessoa. O cálculo do IMC é: peso / (altura * altura), onde a altura deve estar em metros.

nome = input("Digite seu Nome: ")
altura = float(input("Digite a sua altura (m): "))
peso = float(input("Digite o seu peso (kg): "))
imc = peso / (altura * altura)
print(nome,"o seu IMC é ",imc)
