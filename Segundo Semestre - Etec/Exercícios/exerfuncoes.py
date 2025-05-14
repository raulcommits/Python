# EXERCÍCIO 1 - FUNÇÕES: Criar uma "saudacao" para qualquer nome: Feito

def saudacao():
    nome = input("Insira o seu nome: ")
    print(f"Olá {nome}, meus parabéns por ter se inscrito!!!!!!!!!")

saudacao()


# EXERCÍCIO 2 - FUNÇÕES: Criar uma "soma_produto" para somar e multiplicar 2 números: Feito

''' a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
def soma_produto(a, b):
    soma = a + b
    multiplicar = a * b
    return soma, multiplicar

resultado_soma, resultado_multiplicar = soma_produto(a=a, b=b)
print(f"A soma é: {resultado_soma}")
print(f"A produto é: {resultado_multiplicar}") '''


# EXERCÍCIO 3 - FUNÇÕES: Criar uma variável local em uma função e modificá-la: Feito

''' def var_local(y):
    x = 25
    y = x + 5
    return y    # RETORNA "30"
valor = var_local(y=1) # PEGANDO O VALOR DE 'Y' DA FUNÇÃO
print(valor * 3) # TENTANDO ALTERAR O VALOR '''


# EXERCÍCIO 4 - FUNÇÕES: Criar um "conta_palavras" para contar o número de palavras de uma String: Feito

''' frase = input("Escreva uma frase: ")
def conta_palavras(palavra, contairor=" "):
    return len(palavra.split(contairor))
print(f"A quantidade de palavras é: {conta_palavras(frase)}") '''


# EXERCÍCIO 5 - FUNÇÕES: Criar uma função lambda para uma lista dos ^2 em uma lista: Feito

''' numeros = [4, 7, 11, 3, 8, 10]
quadrado = list(map(lambda x: x * x, numeros))
print(quadrado) '''

# EXERCÍCIO 6 - FUNÇÕES: Criar uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci: Feito

''' def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci (n - 2)
for i in range(15):
    print(fibonacci(i), end=" ") '''