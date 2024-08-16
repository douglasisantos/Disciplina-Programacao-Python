#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A.o produto do dobro do primeiro com metade do segundo .
#B. soma do triplo do primeiro com o terceiro.
#C. terceiro elevado ao cubo.

def main():
    inteiro1 = int(input("Digite o primeiro número inteiro: "))
    inteiro2 = int(input("Digite o segundo número inteiro: "))
    real = float(input("Digite um número real: "))
    

    produto = (2 * inteiro1) * (inteiro2 / 2)

    soma = (3 * inteiro1) + real
    
 
    cubo = real ** 3
    

    print(f"O produto do dobro do primeiro com metade do segundo é: {produto:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro é: {soma:.2f}")
    print(f"O terceiro número elevado ao cubo é: {cubo:.2f}")


if __name__ == "__main__":
    main()
