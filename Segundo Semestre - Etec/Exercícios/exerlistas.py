# EXERCÍCIOS "LISTAS" - A: Feito
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0

# for numero in numeros:
#     if numero % 2 != 0:
#         print(numero)

# while i < len(numeros):
#     if numeros[i] % 2 == 0:
#         numeros.pop(i)
#     else:
#         i += 1
# print(numeros)

# EXERCÍCIOS "LISTAS" - B: Feito
# temFruta = input("Digite uma fruta: ")
# frutas = ["Maçã", "Banana", "Morango", "Pera", "Laranja", "Jilo"]
# maisUma = []

# for fruta in frutas:
#     if fruta == temFruta:
#         print("A fruta já está na lista")
#         break
#     else:
#         print("A fruta não está na lista. Adicionando-a")
#         frutas.append(temFruta)
#         break
# print(frutas)

# EXERCÍCIOS "TUPLAS" - A: Feito
# Ceusius = (38.0, 40.0, 15.0, 45.8, 9.0)
# listCeusius = []

# for grau in Ceusius:
#     fahrenheit = (grau * 1.8) + 32
#     listSeusius.append(fahrenheit)
# listSeusius = tuple (listSeusius)
# print(listCeusius)

# EXERCÍCIOS "TUPLAS" - B: Feito
# coordenadas = (-2, 3, -18.2, -4, 7, 94, 20)
# x = 0

# for x in coordenadas:
#     if x > 0:
#         print(f"A coordenada {x} é (supostamente) maior que 0")
#     elif x == 0:
#         print(f"A coordenada {x} é (supostamente) igual 0")
#     else:
#         print(f"A coordenada {x} é (supostamente) menor 0")


# EXERCÍCIOS "DICIONÁRIOS" - A: Feito
# produtos = {"Prato": 15.20, "Celular": 704.00, "Livro": 59.90, "Ventilador": 100.90}
# produtosDesc = {}
# for produto, preco in produtos.items():
#     if preco > 100:
#         produtosDesc = preco - (preco * 0.1)
#         print(f"Os podruto que tem desconto são {produto}: R${produtosDesc:.2f}")

# # EXERCÍCIOS "DICIONÁRIOS" - B: Feito
# livro = {"titulo": "Os Dois Morrem no Final", "autor": "Adam Silvera", "anoPublicacao": 2016}

# if "anoPublicacao" in livro:
#     if livro["anoPublicacao"] > 2000:
#         print(f"{livro['titulo']} foi lançado depois dos anos 2000")