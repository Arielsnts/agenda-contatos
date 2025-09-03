import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
    QLabel, QHeaderView, QHBoxLayout
)

from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional
from classes.agenda import Agenda

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # Atributos da janela e afins
        self.setWindowTitle("Agenda de Contatos")
        self.setFixedSize(750, 650)
        self.move(300, 20)

        # Objeto agenda (lista de Contato)
        self.__agenda = Agenda()

        # ---------- CONTAINER SUPERIOR

        # Texto comum para formulários
        self.texto_form = QLabel("Preencha o formulário:")
        self.texto_form.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Widget para mensagens de erro
        self.erro = QLabel("")
        self.erro.setStyleSheet("color: red; font-weight: bold")

        # ----- MENU DE OPÇÕES

        # Texto do menu
        self.texto_menu = QLabel("Escolha uma opção:")
        self.texto_menu.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Botões
        self.pessoal_add_button = QPushButton("Adicionar contato pessoal")
        self.pessoal_add_button.clicked.connect(self.mostrar_adicionar_pessoal)

        self.pro_add_button = QPushButton("Adicionar contato profissional")
        self.pro_add_button.clicked.connect(self.mostrar_adicionar_pro)

        self.remover_button = QPushButton("Remover pelo nome")
        self.remover_button.clicked.connect(self.mostrar_remover)

        self.alterar_button = QPushButton("Alterar pelo nome")
        self.alterar_button.clicked.connect(self.mostrar_alterar)

        # layout de menu de opções
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.texto_menu)
        menu_layout.addWidget(self.pessoal_add_button)
        menu_layout.addWidget(self.pro_add_button)
        menu_layout.addWidget(self.remover_button)
        menu_layout.addWidget(self.alterar_button)
        menu_layout.addWidget(self.erro)

        # ----- ADICIONAR PESSOAL

        # Widgets
        self.nome_pessoal_add = QLineEdit()
        self.nome_pessoal_add.setPlaceholderText("Digite o nome do contato")

        self.numero_pessoal_add = QLineEdit()
        self.numero_pessoal_add.setPlaceholderText("Digite o número do contato (Ex:XX911112222)")

        self.relacao_pessoal_add = QLineEdit()
        self.relacao_pessoal_add.setPlaceholderText("Digite sua relação com o contato")

        self.submit_pessoal = QPushButton("Adicionar contato")
        self.submit_pessoal.clicked.connect(self.click_adicionar_pessoal)

        # ----- ADICIONAR PROFISSIONAL

        # Widgets
        self.nome_pro_add = QLineEdit()
        self.nome_pro_add.setPlaceholderText("Digite o nome do contato")

        self.numero_pro_add = QLineEdit()
        self.numero_pro_add.setPlaceholderText("Digite o número do contato (Ex:XX911112222)")

        self.email_pro_add = QLineEdit()
        self.email_pro_add.setPlaceholderText("Digite o email do contato")

        self.submit_pro = QPushButton("Adicionar contato")

        # ----- REMOVER CONTATO

        # Widgets
        self.nome_remover = QLineEdit()
        self.nome_remover.setPlaceholderText("Digite o nome do contato a ser removido")

        self.submit_remover = QPushButton("Remover contato")

        # ----- ALTERAR CONTATO
        self.nome_alterar = QLineEdit()
        self.nome_alterar.setPlaceholderText("Digite o nome do contato a ser alterado")

        self.novo_nome = QLineEdit()
        self.novo_nome.setPlaceholderText("Digite o novo nome do contato")

        self.novo_numero = QLineEdit()
        self.novo_numero.setPlaceholderText("Digite o novo número do contato (Ex:XX911112222)")

        self.novo_relacao = QLineEdit()
        self.novo_relacao.setPlaceholderText("Digite a nova relação com o contato")

        self.novo_email = QLineEdit()
        self.novo_email.setPlaceholderText("Digite o novo email do contato")

        self.submit_alterar = QPushButton("Alterar contato")

        # Container que recebe o layout para a região superior
        self.container_superior = QWidget()
        self.container_superior.setLayout(menu_layout)

        # ----- TABELA DE CONTATOS

        # Botões
        self.pessoal_view_button = QPushButton("Visualizar contatos pessoais")
        self.pro_view_button = QPushButton("Visualizar contatos profissionais")

        # Layout dos botões (pra ficarem lado a lado)
        button_out_layout = QHBoxLayout()
        button_out_layout.addWidget(self.pessoal_view_button)
        button_out_layout.addWidget(self.pro_view_button)

        # Tabela

        # Layout da tabela

        # Container que recebe layout dos botões e da tabela
        container_tabela = QWidget()
        container_tabela.setLayout(button_out_layout)

        # ----- PRINCIPAL

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.container_superior)
        main_layout.addWidget(container_tabela)

        # Container
        container_main = QWidget()
        container_main.setLayout(main_layout)
        self.setCentralWidget(container_main)

    # Método que limpa widgets e layouts internos
    def limpar_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            # Se for widget, remove do parent
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

            # Se for um layout interno, limpa recursivamente
            elif item.layout() is not None:
                self.limpar_layout(item.layout())

    # Metódo que alterna para o form de adicionar contato pessoal
    def mostrar_adicionar_pessoal(self):
        layout = self.container_superior.layout()
        
        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato:"))
        layout.addWidget(self.nome_pessoal_add)

        layout.addWidget(QLabel("Número do contato:"))
        layout.addWidget(self.numero_pessoal_add)

        layout.addWidget(QLabel("Relação com o contato:"))
        layout.addWidget(self.relacao_pessoal_add)

        layout.addWidget(self.submit_pessoal)

        layout.addWidget(self.erro)

    def mostrar_adicionar_pro(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato:"))
        layout.addWidget(self.nome_pro_add)

        layout.addWidget(QLabel("Número do contato:"))
        layout.addWidget(self.numero_pro_add)

        layout.addWidget(QLabel("Email do contato:"))
        layout.addWidget(self.email_pro_add)

        layout.addWidget(self.submit_pro)
    
    def mostrar_remover(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato a ser removido:"))
        layout.addWidget(self.nome_remover)

        layout.addWidget(self.submit_remover)

    def mostrar_alterar(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        texto = QLabel("Preencha o formulário (Campos vazios não serão alterados):")
        texto.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(texto)

        layout.addWidget(QLabel("Nome do contato a ser alterado:"))
        layout.addWidget(self.nome_alterar)

        layout.addWidget(QLabel("Novo nome do contato:"))
        layout.addWidget(self.novo_nome)

        layout.addWidget(QLabel("Novo número do contato:"))
        layout.addWidget(self.novo_numero)

        layout.addWidget(QLabel("Relação com o contato (Vazio se for profissional):"))
        layout.addWidget(self.novo_relacao)

        layout.addWidget(QLabel("Email do contato (Vazio se for pessoal):"))
        layout.addWidget(self.novo_email)

        layout.addWidget(self.submit_alterar)

    # Método que retorna para o menu de opções
    def voltar_menu(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Reconstrói os widgets do menu
        layout.addWidget(self.texto_menu)
        layout.addWidget(self.pessoal_add_button)
        layout.addWidget(self.pro_add_button)
        layout.addWidget(self.remover_button)
        layout.addWidget(self.alterar_button)

    def click_adicionar_pessoal(self):
        nome = self.nome_pessoal_add.text()
        numero = self.nome_pessoal_add.text()
        relacao = self.nome_pessoal_add.text()

        if not nome or not numero or not relacao:
            self.erro.setText("Preencha todos os campos!")
            return

        if len(numero) != 11 or not numero.isdigit():
            self.erro.setText("O número deve conter exatamente 11 dígitos seguidos")
            return

        self.erro.clear()

        self.__agenda.adicionarContato(ContatoPessoal(nome, numero, relacao))

        # self.__agenda.imprimirAgenda()

        self.nome_pessoal_add.clear()
        self.numero_pessoal_add.clear()
        self.relacao_pessoal_add.clear()


def iniciarApp():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())