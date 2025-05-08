# EXERCÍCIO 3 - ler e exibir o conteúdo desse arquivo, e depois, adicionar novos alunos
import csv

with open('Exercícios Leitura de Arquivos\\alunos.csv', 'r') as arquivo:
    estudantes = csv.reader(arquivo)
    for linha in estudantes:
        print(linha)

nome = input("Digite o nome: ")
idade = int(input("Digite o idade: "))
nota = int(input("Digite o nota: "))
aluno = [nome, idade, nota]

with open('Exercícios Leitura de Arquivos\\alunos.csv', 'a', newline="\n") as arquivo:
    novoAluno = csv.writer(arquivo)
    novoAluno.writerow(aluno)
    print("Aluno cadastrado com sucesso!")