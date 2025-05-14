# EXERCÍCIO 2.1 - Escrever um Script que: Obter & imprimir o diretório atual; Listar os arquivos um por um; Criar um novo diretório e mandar uma mensagem de confirmação: FEITO
# EXERCÍCIO 2.2 - Executar o código: FEITO

import os

arquivos = os.listdir()
for i in arquivos:
    print(f"{i}")

novoDiretorio = "novo_diretorio"

os.mkdir(novoDiretorio)
print("Um novo diretório foi criado com sucesso")