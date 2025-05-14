# EXERCÍCIO 1 - Ler um arquivo chamado "poema.txt" e exibir seu conteúdo: FEITO

with open('poema.txt', 'r') as arquivo:
    versos = arquivo.read()
    print(versos)