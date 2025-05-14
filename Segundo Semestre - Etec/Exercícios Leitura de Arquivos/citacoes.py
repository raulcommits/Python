# EXERCÍCIO 2 - Script que permita ao usuário a capacidade de escrever citações, sem sobrescrever as existentes: FEITO

citacao = input("Escreva uma citação: ")

with open('citacoes.txt', 'a') as arquivo:
    arquivo.write(citacao + "\n")

with open('citacoes.txt', 'r') as arquivoConferido:    
    conteudo = arquivoConferido.read()
    print(conteudo)
