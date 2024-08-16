palavras_proibidas = ['PALAVRA','PALAVRA2','PALAVRA3','PALAVRA4']

frases = input('Digite uma frase:').upper()
frases_vetor = frases.split()

for palavra in frases_vetor:
    if palavra in palavras_proibidas:
        print(f"você usou palavra proibida...{palavra}")
    
