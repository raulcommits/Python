import mysql.connector
from PyQt5 import uic, QtWidgets

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "etecembu@123",
    database = "bloco"
)

def main():
    campoId = bloco.id.text()
    print("Id: ", campoId)
    campoNome = bloco.nome.text()
    print("Nome: ", campoNome)
    campoEmail = bloco.email.text()
    print("Email: ", campoEmail)
    campoTelefone = bloco.telefone.text()
    print("Telefone: ", campoTelefone)
    
    tipoTelefone = ""

    if bloco.residencial.isChecked():
        print("Tipo de telefone é residencial ")
        tipoTelefone = "Residencial"
    elif bloco.celular.isChecked():
        print("Tipo de telefone é Celular")
        tipoTelefone = "Celular"
    else:
        print("Informe o tipo de telefone")
        tipoTelefone = "Não informado"
        
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO contatinhos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)"
    dados = (str(campoNome), str(campoEmail), str(campoTelefone), tipoTelefone)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    
    bloco.nome.setText("");
    bloco.email.setText("");
    bloco.telefone.setText("");
    
    print("Contato cadastrado com sucesso")
    
def telaConsulta():
    blocoConsultar.show()
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatinhos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    
    blocoConsultar.tabela_contatinhos.setRowCount(len(contatos_lidos))
    blocoConsultar.tabela_contatinhos.setColumnCount(5)
    
    for i in range(0, len(contatos_lidos)):
        for j in range(0, 5):
            blocoConsultar.tabela_contatinhos.setItem(i, j, QtWidgets.QTableWidgetItem(str(contatos_lidos[i][j])))

def alterarContato():
    linhaContato = blocoConsultar.tabela_contatinhos.currentRow()
    blocoConsultar.tabela_contatinhos.updateRow(linhaContato)
    
    cursor = banco.cursor()
    comando_SQL = "SELECT if FROM contatinhos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato]
    cursor.execute("UPDATE FROM contatinhos WHERE id=" + str(valorId))
    banco.commit()
    

def excluirContato():
    linhaContato = blocoConsultar.tabela_contatinhos.currentRow()
    blocoConsultar.tabela_contatinhos.removeRow(linhaContato)
    
    cursor = banco.cursor()
    comando_SQL = "SELECT id FROM contatinhos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato][0]
    cursor.execute("DELETE FROM contatinhos WHERE id=" + str(valorId))
    banco.commit()

app=QtWidgets.QApplication([])

bloco=uic.loadUi("bloco_de_notas.ui")

bloco.enviacao.clicked.connect(main)

blocoConsultar=uic.loadUi("listaContatos.ui")
bloco.btnConsultar.clicked.connect(telaConsulta)
blocoConsultar.exclusaoContato.clicked.connect(excluirContato)

# Fazer o programa funcionar
bloco.show()
app.exec()