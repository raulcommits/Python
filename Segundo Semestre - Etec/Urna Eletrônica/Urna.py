import csv


# ===> Autenticação com senha
acesso = False
senhaUrna = 3232
contador = 1


### ===> Funções
def verificarSenha():
    global acesso
    if senhaDigitada == senhaUrna:
        acesso = True
        return print("Acesso permitido!\n")
    else:
        print("Senha incorreta! Tente novamente.\n")
        verificarSenha()

def opcoesMenu():
    print("Escolha uma das opções:\n\t1 - Lista de candidatos\n\t2 - Cadastrar candidatos\n\t3 - Iniciar votação\n\t4 - Checagem dos votos\n\t5 - Sair\n")
    opcao = input("Selecione uma opção: ")
    print("\n")

    if opcao == "1":
        print("Lista de candidatos:")
        lerCanditados()
        print("\n")
    elif opcao == "2":
        print("Cadastro de candidato:")
        cadastrarCandidatos()
    elif opcao == "3":
        print("Iniciando votação...")
        iniciarVotacao()
    elif opcao == "4":
        print("Checagem de votos:")
        checarVotos()
        n1 = 1
    elif opcao == "5":
        sair()
    else:
        print("Opção inválida!")

def lerCanditados():
    with open("candidatos.csv", "r") as arquivo:
        candidatos = csv.reader(arquivo)
        global contador
        for candidato in candidatos:
            print(f"\tNº: {contador} \t Candidato:  {candidato[0]} \t\t Partido:  {candidato[1]} \t\t Número:  {candidato[2]}")
            contador+=1

def cadastrarCandidatos():
    nome = input("Nome: ")
    partido = input("Partido: ")
    numero = input("Número: ")
    candidato = [nome, partido, numero]

    with open("candidatos.csv", "a", newline='') as arquivo:
        dado = csv.writer(arquivo)
        dado.writerow(candidato)
        print("Candidato cadastrado com sucesso!\n")
    print(candidato)

def iniciarVotacao(): #Mexer aqui
    # Pedir senha novamente
    # verificarSenha()
    print("\nEscolha um candidatos: ")
    lerCanditados()
    candidatoEscolhido = int(input("Escolha um candidato: "))
    if candidatoEscolhido == 1:
        cand1 = 0
        cand1+= 1
        print("\nVoto registrado!\n")
        print(cand1)
    elif candidatoEscolhido == 2:
        cand2 = 0
        cand2+= 1
        print("\nVoto registrado!\n")
        print(cand2)

    continuar = input("Deseja votar novamente? (S ou N):").upper()
    if continuar == "S":
        iniciarVotacao()
    elif continuar == "N":
        opcoesMenu()
    else:
        opcoesMenu()

def checarVotos(): #Mexer aqui
    print("FALTA MEXER AQUI")

def sair():
    print("Saindo..\n")
    exit()


### ===> Tela de inicio
print("\nBem vindo a eleição!")
print("Pra começar, insira a senha da Urna Eletrônica: \n")

senhaDigitada = int(input("Digite a senha: "))
verificarSenha()

while acesso == True:
    opcoesMenu()