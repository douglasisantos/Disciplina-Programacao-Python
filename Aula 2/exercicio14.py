
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Função principal
def main():
    # Solicita o peso dos peixes ao usuário
    peso = float(input("Digite o peso dos peixes (em quilos): "))
    
    # Define o limite estabelecido
    limite = 50
    multa_por_quilo_excedente = 4.00
    
    # Calcula o excesso se houver
    if peso > limite:
        excesso = peso - limite
        multa = excesso * multa_por_quilo_excedente
    else:
        excesso = 0
        multa = 0
    
    # Exibe os resultados
    if excesso > 0:
        print(f"Peso dos peixes: {peso:.2f} kg")
        print(f"Excesso de peso: {excesso:.2f} kg")
        print(f"Multa a pagar: R$ {multa:.2f}")
    else:
        print("Não houve excesso de peso. Não há multa a pagar.")
    
# Executa a função principal
if __name__ == "__main__":
    main()
