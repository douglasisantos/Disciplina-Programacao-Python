#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#Obs.: Salário Bruto - Descontos = Salário Líquido.


# Função principal
def main():
    # Solicita o valor ganho por hora e o número de horas trabalhadas no mês ao usuário
    valor_por_hora = float(input("Digite quanto você ganha por hora: R$ "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    
    # Calcula o salário bruto
    salario_bruto = valor_por_hora * horas_trabalhadas
    
    # Calcula os descontos
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato = salario_bruto * 0.05
    desconto_ir = salario_bruto * 0.11
    
    # Calcula o salário líquido
    salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato + desconto_ir)
    
    # Exibe os resultados
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto do INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
    print(f"Desconto do Imposto de Renda: R$ {desconto_ir:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Executa a função principal
if __name__ == "__main__":
    main()
