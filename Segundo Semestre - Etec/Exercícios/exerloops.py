''' while True:
    nome = input("Insira um nome: ")
    opcao = input("Deseja cadastrar mais?")
    nomes.append(nome)
    if opcao == 's':
        pass
    else:
        break

for i in range(5, 20):
    if i % 2 == 0:
        continue
    print(i) '''

# EXERCÍCIO 1 (Controle de Fluxo Adicional) - break em um Loop While: Feito
''' numeros = []
while True:
    numero = input("Insira um número de 0 à 9: ")
    numeros.append(numero)
    if (numero != '0'):
        pass
    else:
        break
print(numeros) '''

# EXERCÍCIO 2 (Controle de Fluxo Adicional) - continue em um Loop While: Feito
''' for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i) '''

# EXERCÍCIO 3 (Controle de Fluxo Adicional) - pass em um Condicional: Feito
''' numero = input("Digite um número: ")
verfnumero = int(numero)
while True:
    if (verfnumero % 2 == 0):
        pass
    else:
        impar = ("O número " + numero + " é impar")
        print(impar) '''