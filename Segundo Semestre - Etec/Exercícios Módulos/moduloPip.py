# EXERCÍCIO 3.1 - Instalar o módulo "requests": FEITO
# EXERCÍCIO 3.2 - Escrever um Script que: Use o requests para fazer o método GET (HTTP) na API do Github; Verificar o código de status da resposta e imprimi-la se for bem sucedido; Extrair e imprimir  
# EXERCÍCIO 3.3 - Executar o Script e verificar a saída: 

import requests

resposta = requests.get('https://api.github.com/')
print(resposta.status_code)
print(resposta.json())