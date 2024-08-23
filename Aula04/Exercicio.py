# Função para gerar o e-mail a partir do nome completo
def gerar_email(nome_completo):
    partes = nome_completo.split()
    if len(partes) < 2:
        return None  # Retorna None se o nome completo não contiver pelo menos um nome e um sobrenome
    sobrenome = partes[-1]
    nome = partes[0]
    return f"{sobrenome.lower()}.{nome.lower()}@ufn.edu.br"

# Criando um conjunto para armazenar e-mails únicos
emails = set()

# Coletando 4 nomes completos e gerando e-mails
for _ in range(4):
    nome_completo = input('Digite um nome completo: ')
    email = gerar_email(nome_completo)
    if email:
        if email not in emails:
            emails.add(email)
        else:
            print(f"O e-mail {email} já foi adicionado.")

# Convertendo o conjunto de e-mails para uma lista e ordenando
lista_emails = sorted(emails)

# Imprimindo os e-mails gerados
print("E-mails gerados:")
for email in lista_emails:
    print(email)
