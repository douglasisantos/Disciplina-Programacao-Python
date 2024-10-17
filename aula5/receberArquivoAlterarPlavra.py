def substituir_palavra():
    # Solicitar ao usuário o caminho e nome do arquivo
    arquivo = input("Digite o caminho e nome do arquivo: ")
    
    # Solicitar ao usuário a palavra ou expressão a ser substituída
    palavra_antiga = input("Digite a palavra ou expressão a ser substituída: ")
    palavra_nova = input("Digite a nova palavra ou expressão: ")

    try:
        # Abrir o arquivo para leitura
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        
        # Substituir a palavra ou expressão
        conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)
        
        # Abrir o arquivo para escrita e salvar as modificações
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write(conteudo_modificado)
        
        print(f"A palavra ou expressão '{palavra_antiga}' foi substituída por '{palavra_nova}' com sucesso.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e o nome do arquivo e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
substituir_palavra()
