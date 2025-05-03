# EXERCÍCIO 3 - ler e exibir o conteúdo desse arquivo, e depois, adicionar novos alunos

import csv

dadosAluno = [
    ['Nome', 'Idade', 'Nota'],
    ['Beatriz', 14, 7],
    ['Donald', 15, 5],
    ['Heitor', 13, 9],
    ['Mirela', 14, 8]
]

with open('alunos.csv', 'w', newline='') as arquivo:
    aluno = csv.writer(arquivo)
    aluno.writerows(dadosAluno)

with open('alunos.csv', 'r') as arquivo:
    estudantes = csv.reader(arquivo)
    for linha in estudantes:
        print(linha)