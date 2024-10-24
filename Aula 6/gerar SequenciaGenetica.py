import random

def gerar_sequencia(num_nucleotideos):
    nucleotideos = ['A', 'C', 'G', 'T']
    sequencia = ''.join(random.choices(nucleotideos, k=num_nucleotideos))
    return sequencia

def salvar_em_arquivo(sequencia, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        file.write(sequencia)

if __name__ == "__main__":
    num_nucleotideos = 10_000_000  # 10 milhões
    sequencia = gerar_sequencia(num_nucleotideos)
    salvar_em_arquivo(sequencia, 'sequencia_10milhoes.txt')
    print("Sequência gerada e salva em 'sequencia_10milhoes.txt'")
