import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# Criando a aplicação
app = QApplication(sys.argv)

# Função para o botão
def botaoClicado():
    print("Você clicou no botão")

# Criando a janela principal
janela_no_diminutivo = QWidget()
janela_no_diminutivo.setWindowTitle("Primeira Aplicação Front-End")
janela_no_diminutivo.setGeometry(50, 200, 350, 150)

# Estilizando o Botão
with open('estilo.qss', 'r') as arquivo_qss:
    estilo = arquivo_qss.read()
    app.setStyleSheet(estilo)

# Criando um label
textoLabel = QLabel("Clique no botão abaixo", janela_no_diminutivo)
textoLabel.move(130, 30)

# Criando um botão
botao = QPushButton("Um Botão", janela_no_diminutivo)
botao.setObjectName("botaoCustomizado")
botao.move(450, 500)

botao2 = QPushButton("Mais um botão", janela_no_diminutivo)
botao2.setObjectName("botaoVestido")
botao2.move(900, 500)

botao3 = QPushButton("O terceiro butão", janela_no_diminutivo)
botao3.setObjectName("botaoColoridinho")
botao3.move(1350, 500)

# Estilizando o botão

# chamando a função do botão
botao.clicked.connect(botaoClicado)
botao2.clicked.connect(botaoClicado)
botao3.clicked.connect(botaoClicado)

# Exibindo a janelinha
janela_no_diminutivo.showMaximized()

# Iniciandoo o loop de eventos
sys.exit(app.exec_())