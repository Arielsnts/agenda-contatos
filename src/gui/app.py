import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QLabel, QHeaderView, QHBoxLayout
)

from PyQt5.QtCore import Qt

from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional
from classes.agenda import Agenda

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- CONFIG JANELA
        self.setWindowTitle("Agenda de Contatos")
        self.setFixedSize(1000, 650)
        self.move(300, 20)

        self.__agenda = Agenda()

        # --- DEBUG: Adicionando contatos iniciais
        self.__agenda.adicionarContato(ContatoPessoal("Ariel", "79991234567", "Amigo"))
        self.__agenda.adicionarContato(ContatoPessoal("Lucas", "79992345678", "Colega"))
        self.__agenda.adicionarContato(ContatoPessoal("Maria", "79993456789", "Prima"))

        self.__agenda.adicionarContato(ContatoProfissional("Felipe", "79994567890", "felipe@gmail.com"))
        self.__agenda.adicionarContato(ContatoProfissional("João", "79995678901", "joao@empresa.com"))
        self.__agenda.adicionarContato(ContatoProfissional("Ana", "79996789012", "ana@trabalho.com"))

        # --- ESTILO PADRÃO BOTÕES
        self.botao_style = """
        QPushButton {
            background-color: lightgray;
            border-radius: 10px;
            padding: 8px;
            font-size: 14px;
            min-width: 200px;
        }
        QPushButton:hover {
            background-color: gray;
            color: white;
        }
        """

        # --- LABELS
        self.texto_form = QLabel("Preencha o formulário:")
        self.texto_form.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.erro = QLabel("")
        self.erro.setStyleSheet("color: red; font-weight: bold")

        # --- BOTÃO VOLTAR
        self.volta_button = QPushButton("Voltar pro menu")
        self.volta_button.setStyleSheet(self.botao_style)
        self.volta_button.clicked.connect(self.voltar_menu)

        # --- MENU PRINCIPAL
        self.texto_menu = QLabel("Escolha uma opção:")
        self.texto_menu.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.add_button = QPushButton("Adicionar Contato")
        self.add_button.setStyleSheet(self.botao_style)
        self.add_button.clicked.connect(self.mostrar_menu_add)

        self.remover_button = QPushButton("Remover Contato")
        self.remover_button.setStyleSheet(self.botao_style)
        self.remover_button.clicked.connect(self.mostrar_remover)

        self.alterar_button = QPushButton("Alterar Contato")
        self.alterar_button.setStyleSheet(self.botao_style)
        self.alterar_button.clicked.connect(self.mostrar_alterar)

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.texto_menu)
        menu_layout.addWidget(self.add_button)
        menu_layout.addWidget(self.remover_button)
        menu_layout.addWidget(self.alterar_button)
        menu_layout.addWidget(self.erro)

        # --- ADICIONAR CONTATOS PESSOAIS
        self.nome_pessoal_add = QLineEdit()
        self.nome_pessoal_add.setPlaceholderText("Digite o nome do contato")

        self.numero_pessoal_add = QLineEdit()
        self.numero_pessoal_add.setPlaceholderText("Digite o número do contato (Ex:XX911112222)")

        self.relacao_pessoal_add = QLineEdit()
        self.relacao_pessoal_add.setPlaceholderText("Digite sua relação com o contato")

        self.submit_pessoal = QPushButton("Adicionar contato")
        self.submit_pessoal.setStyleSheet(self.botao_style)
        self.submit_pessoal.clicked.connect(self.click_adicionar_pessoal)

        # --- ADICIONAR CONTATOS PROFISSIONAIS
        self.nome_pro_add = QLineEdit()
        self.nome_pro_add.setPlaceholderText("Digite o nome do contato")

        self.numero_pro_add = QLineEdit()
        self.numero_pro_add.setPlaceholderText("Digite o número do contato (Ex:XX911112222)")

        self.email_pro_add = QLineEdit()
        self.email_pro_add.setPlaceholderText("Digite o email do contato")

        self.submit_pro = QPushButton("Adicionar contato")
        self.submit_pro.setStyleSheet(self.botao_style)
        self.submit_pro.clicked.connect(self.click_adicionar_pro)

        # --- REMOVER CONTATO
        self.nome_remover = QLineEdit()
        self.nome_remover.setPlaceholderText("Digite o nome do contato a ser removido")

        self.submit_remover = QPushButton("Remover contato")
        self.submit_remover.setStyleSheet(self.botao_style)
        self.submit_remover.clicked.connect(self.click_remover)

        # --- ALTERAR CONTATO
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
        self.submit_alterar.setStyleSheet(self.botao_style)
        self.submit_alterar.clicked.connect(self.click_alterar)

        # --- CONTAINER SUPERIOR
        self.container_superior = QWidget()
        self.container_superior.setLayout(menu_layout)

        # --- BOTÕES VISUALIZAÇÃO
        self.todos_view_button = QPushButton("Visualizar todos os contatos")
        self.todos_view_button.setStyleSheet(self.botao_style)
        self.todos_view_button.clicked.connect(self.mostrar_todos)

        self.pessoal_view_button = QPushButton("Visualizar contatos pessoais")
        self.pessoal_view_button.setStyleSheet(self.botao_style)
        self.pessoal_view_button.clicked.connect(self.mostrar_pessoais)

        self.pro_view_button = QPushButton("Visualizar contatos profissionais")
        self.pro_view_button.setStyleSheet(self.botao_style)
        self.pro_view_button.clicked.connect(self.mostrar_profissionais)

        button_out_layout = QHBoxLayout()
        button_out_layout.addWidget(self.pessoal_view_button)
        button_out_layout.addWidget(self.pro_view_button)
        button_out_layout.addWidget(self.todos_view_button)

        # --- TABELA DE CONTATOS
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Número", "Relação/Email"])

        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        self.tabela.setColumnWidth(0, 270)
        self.tabela.setColumnWidth(1, 270)
        self.tabela.setColumnWidth(2, 410)

        self.tabela.setStyleSheet("font-size: 14px;")

        self.titulo_tabela = QLabel("Contatos pessoais:")
        self.titulo_tabela.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.mostrar_pessoais()

        inferior_layout = QVBoxLayout()
        inferior_layout.addLayout(button_out_layout)
        inferior_layout.addWidget(self.titulo_tabela)
        inferior_layout.addWidget(self.tabela)

        # --- CONTAINER INFERIOR
        self.container_inferior = QWidget()
        self.container_inferior.setLayout(inferior_layout)

        # --- LAYOUT E CONTAINER PRINCIPAL
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.container_superior)
        main_layout.addWidget(self.container_inferior)

        container_main = QWidget()
        container_main.setLayout(main_layout)
        self.setCentralWidget(container_main)

    # --- MÉTODOS DE ALTERAÇÃO DE TELAS
    def limpar_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget: widget.setParent(None)
            elif item.layout(): self.limpar_layout(item.layout())

    # Métodos de alternar formulários
    def mostrar_menu_add(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(QLabel("Escolha o tipo de contato:"))

        pessoal_button = QPushButton("Pessoal")
        pessoal_button.setStyleSheet(self.botao_style)
        pessoal_button.clicked.connect(self.mostrar_adicionar_pessoal)

        pro_button = QPushButton("Profissional")
        pro_button.setStyleSheet(self.botao_style)
        pro_button.clicked.connect(self.mostrar_adicionar_pro)

        layout.addWidget(pessoal_button)
        layout.addWidget(pro_button)
        layout.addWidget(self.volta_button)

    def mostrar_adicionar_pessoal(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato:"))
        layout.addWidget(self.nome_pessoal_add)

        layout.addWidget(QLabel("Número do contato:"))
        layout.addWidget(self.numero_pessoal_add)

        layout.addWidget(QLabel("Relação com o contato:"))
        layout.addWidget(self.relacao_pessoal_add)

        layout.addWidget(self.submit_pessoal)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    def mostrar_adicionar_pro(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato:"))
        layout.addWidget(self.nome_pro_add)

        layout.addWidget(QLabel("Número do contato:"))
        layout.addWidget(self.numero_pro_add)

        layout.addWidget(QLabel("Email do contato:"))
        layout.addWidget(self.email_pro_add)

        layout.addWidget(self.submit_pro)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    def mostrar_remover(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato a ser removido:"))
        layout.addWidget(self.nome_remover)

        layout.addWidget(self.submit_remover)

        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    def mostrar_alterar(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

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

        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    def voltar_menu(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(self.texto_menu)

        layout.addWidget(self.add_button)

        layout.addWidget(self.remover_button)

        layout.addWidget(self.alterar_button)

        self.erro.clear()

    # --- MÉTODOS DE FUNCIONAMENTO
    def click_adicionar_pessoal(self):
        nome = self.nome_pessoal_add.text()
        numero = self.numero_pessoal_add.text()
        relacao = self.relacao_pessoal_add.text()

        if not nome or not numero or not relacao:
            self.erro.setText("Erro: Preencha todos os campos!")
            return

        self.erro.clear()

        try:
            self.__agenda.adicionarContato(ContatoPessoal(nome, numero, relacao))
        except ValueError as e:
            self.erro.setText(str(e))
            return

        self.nome_pessoal_add.clear()
        self.numero_pessoal_add.clear()
        self.relacao_pessoal_add.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    def click_adicionar_pro(self):
        nome = self.nome_pro_add.text()
        numero = self.numero_pro_add.text()
        email = self.email_pro_add.text()

        if not nome or not numero or not email:
            self.erro.setText("Erro: Preencha todos os campos.")
            return

        self.erro.clear()

        try:
            self.__agenda.adicionarContato(ContatoProfissional(nome, numero, email))
        except ValueError as e:
            self.erro.setText(str(e))
            return

        self.nome_pro_add.clear()
        self.numero_pro_add.clear()
        self.email_pro_add.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    def click_remover(self):
        nome = self.nome_remover.text()

        if not nome:
            self.erro.setText("Erro: Preencha todos os campos.")
            return

        self.erro.clear()

        try:
            self.__agenda.removerContato(nome)
        except LookupError as e:
            self.erro.setText(str(e))
            return

        self.nome_remover.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    def click_alterar(self):
        nome_alterar = self.nome_alterar.text()

        if not nome_alterar:
            self.erro.setText("Erro: Preencha pelo menos o primeiro campo.")
            return

        self.erro.clear()

        nome = self.novo_nome.text()
        numero = self.novo_numero.text()
        relacao = self.novo_relacao.text()
        email = self.novo_email.text()

        try:
            self.__agenda.alterarContato(nome_alterar, nome, numero, relacao, email)
        except (LookupError, ValueError) as e:
            self.erro.setText(str(e))
            return

        self.nome_alterar.clear()
        self.novo_nome.clear()
        self.novo_numero.clear()
        self.novo_relacao.clear()
        self.novo_email.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    # --- MÉTODOS DE ATUALIZAÇÃO DE TABELA
    def mostrar_pessoais(self):
        self.titulo_tabela.setText("Contatos pessoais:")
        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        pessoais = [c for c in contatos if isinstance(c, ContatoPessoal)]
        pessoais.sort(key=lambda c: c.getNome().upper())

        for c in pessoais:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getRelacao()))

    def mostrar_profissionais(self):
        self.titulo_tabela.setText("Contatos profissionais:")
        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        pro = [c for c in contatos if isinstance(c, ContatoProfissional)]
        pro.sort(key=lambda c: c.getNome().upper())

        for c in pro:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getEmail()))

    def mostrar_todos(self):
        self.titulo_tabela.setText("Todos os contatos:")
        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        contatos.sort(key=lambda c: c.getNome().upper())

        for c in contatos:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            if isinstance(c, ContatoPessoal):
                self.tabela.setItem(row, 2, QTableWidgetItem(c.getRelacao()))
            else:
                self.tabela.setItem(row, 2, QTableWidgetItem(c.getEmail()))

# --- FUNÇÃO PRINCIPAL
def iniciarApp():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())
    