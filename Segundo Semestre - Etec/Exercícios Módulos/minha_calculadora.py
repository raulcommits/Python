# EXERCÍCIO 1.1 - Criando um módulo chamado "minha_calculadora": FEITO

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if(b == 0):
        print("O segundo número não pode ser igual a 0")

    return a / b

resultado_soma = soma(2, 3)
resultado_subtracao = subtracao(5, 1)
resultado_multiplicacao = multiplicacao(7, 3)
resultado_divisao = divisao(8, 2)

# print(f"A soma é: {resultado_soma}")
# print(f"A subtração é: {resultado_subtracao}")
# print(f"O produto é: {resultado_multiplicacao}")
# print(f"A divisão é: {resultado_divisao}")