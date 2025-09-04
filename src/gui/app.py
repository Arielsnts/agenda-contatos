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

        # Atributos da janela e afins
        self.setWindowTitle("Agenda de Contatos")
        self.setFixedSize(1000, 650)
        self.move(300, 20)

        # Objeto agenda (lista de Contato)
        self.__agenda = Agenda()

        # ----- DEBUG

        # Adicionando contatos pessoais
        self.__agenda.adicionarContato(ContatoPessoal("Ariel", "79991234567", "Amigo"))
        self.__agenda.adicionarContato(ContatoPessoal("Lucas", "79992345678", "Colega"))
        self.__agenda.adicionarContato(ContatoPessoal("Maria", "79993456789", "Prima"))

        # Adicionando contatos profissionais
        self.__agenda.adicionarContato(ContatoProfissional("Felipe", "79994567890", "felipe@gmail.com"))
        self.__agenda.adicionarContato(ContatoProfissional("João", "79995678901", "joao@empresa.com"))
        self.__agenda.adicionarContato(ContatoProfissional("Ana", "79996789012", "ana@trabalho.com"))

        # ---------- CONTAINER SUPERIOR

        # Texto comum para formulários
        self.texto_form = QLabel("Preencha o formulário:")
        self.texto_form.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Widget para mensagens de erro
        self.erro = QLabel("")
        self.erro.setStyleSheet("color: red; font-weight: bold")

        # Botão para voltar pro menu
        self.volta_button = QPushButton("Voltar pro menu")
        self.volta_button.clicked.connect(self.voltar_menu)

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
        self.submit_pro.clicked.connect(self.click_adicionar_pro)

        # ----- REMOVER CONTATO

        # Widgets
        self.nome_remover = QLineEdit()
        self.nome_remover.setPlaceholderText("Digite o nome do contato a ser removido")

        self.submit_remover = QPushButton("Remover contato")
        self.submit_remover.clicked.connect(self.click_remover)

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
        self.submit_alterar.clicked.connect(self.click_alterar)

        # Container que recebe o layout para a região superior
        self.container_superior = QWidget()
        self.container_superior.setLayout(menu_layout)

        # -------- CONTAINER INFERIOR

        # Botões
        self.pessoal_view_button = QPushButton("Visualizar contatos pessoais")
        self.pessoal_view_button.clicked.connect(self.mostrar_pessoais)

        self.pro_view_button = QPushButton("Visualizar contatos profissionais")
        self.pro_view_button.clicked.connect(self.mostrar_profissionais)

        # Layout dos botões (pra ficarem lado a lado)
        button_out_layout = QHBoxLayout()
        button_out_layout.addWidget(self.pessoal_view_button)
        button_out_layout.addWidget(self.pro_view_button)

        # ----- TABELA DE CONTATOS

        # -- Configuração da tabela
        self.tabela = QTableWidget()
        # Colunas
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Número", "Relação/Email"])
        # Configuração pra tabela não ser redimensionada
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.tabela.setStyleSheet("font-size: 14px;")

        # Largura das colunas
        self.tabela.setColumnWidth(0, 270)
        self.tabela.setColumnWidth(1, 270)
        self.tabela.setColumnWidth(2, 410)

        # Título da tabela (inicia em contatos pessoais)
        self.titulo_tabela = QLabel("Contatos pessoais:")
        self.titulo_tabela.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.mostrar_pessoais()

        # Layout vertical para o container inferior
        inferior_layout = QVBoxLayout()
        inferior_layout.addLayout(button_out_layout)  
        inferior_layout.addWidget(self.titulo_tabela)
        inferior_layout.addWidget(self.tabela)

        # Container que recebe layout inferior
        self.container_inferior = QWidget()
        self.container_inferior.setLayout(inferior_layout)

        # ----- PRINCIPAL

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.container_superior)
        main_layout.addWidget(self.container_inferior)

        # Container principal
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

    # ----- MÉTODOS PARA ALTERNAR ENTRE AS OPÇÕES

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

        layout.addWidget(self.volta_button)

        layout.addWidget(self.erro)

    # Metódo que alterna para o form de adicionar contato profissional
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

        layout.addWidget(self.volta_button)

        layout.addWidget(self.erro)

    # Metódo que alterna para o form de remover contato
    def mostrar_remover(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        layout.addWidget(self.texto_form)

        layout.addWidget(QLabel("Nome do contato a ser removido:"))
        layout.addWidget(self.nome_remover)

        layout.addWidget(self.submit_remover)

        layout.addWidget(self.volta_button)

        layout.addWidget(self.erro)

    # Metódo que alterna para o form de alterar contato
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

        layout.addWidget(self.volta_button)

        layout.addWidget(self.erro)

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

        self.erro.clear()

        # debug
        # print("-" * 10)
        # self.__agenda.imprimirAgenda()
        # print("-" * 10)
    
    # ----- MÉTODOS PARA O FUNCIONAMENTO DOS BOTÕES

    # Método para o botão de adicionar pessoal
    def click_adicionar_pessoal(self):
        nome = self.nome_pessoal_add.text()
        numero = self.numero_pessoal_add.text()
        relacao = self.relacao_pessoal_add.text()

        if not nome or not numero or not relacao:
            self.erro.setText("Erro: Preencha todos os campos!")
            return

        if len(numero) != 11 or not numero.isdigit():
            self.erro.setText("Erro: O número deve conter exatamente 11 dígitos seguidos")
            return
        
        if numero[0] != "9":
           self.erro.setText("Erro: O número deve começar com 9 após o DDD.")
           return

        self.erro.clear()

        self.__agenda.adicionarContato(ContatoPessoal(nome, numero, relacao))

        self.nome_pessoal_add.clear()
        self.numero_pessoal_add.clear()
        self.relacao_pessoal_add.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    # Método para o botão de adicionar profissional
    def click_adicionar_pro(self):
        nome = self.nome_pro_add.text()
        numero = self.numero_pro_add.text()
        email = self.email_pro_add.text()

        if not nome or not numero or not email:
            self.erro.setText("Erro: Preencha todos os campos.")
            return

        if len(numero) != 11 or not numero.isdigit():
            self.erro.setText("Erro: O número deve conter exatamente 11 dígitos seguidos.")
            return

        self.erro.clear()

        self.__agenda.adicionarContato(ContatoProfissional(nome, numero, email))

        self.nome_pro_add.clear()
        self.numero_pro_add.clear()
        self.email_pro_add.clear()

        self.voltar_menu()
        self.mostrar_pessoais()

    # Método para o botão remover
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
        
        self.__agenda.imprimirAgenda()
        
        self.nome_remover.clear()
        self.voltar_menu()
        self.mostrar_pessoais()

    # Método para o botão alterar
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

    # ----- MÉTODOS PARA ATUALIZAÇÃO DA TABELA

    # Método pra atualizar a tabela de contatos pessoais
    def mostrar_pessoais(self):
        self.titulo_tabela.setText("Contatos pessoais:")

        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda() 
        except ValueError:
            contatos = []

        # filtro de contatos pessoais
        pessoais = [c for c in contatos if isinstance(c, ContatoPessoal)] 
        # Ordem alfabética
        pessoais.sort(key=lambda c: c.getNome().upper())

        for contato in pessoais:
            row_position = self.tabela.rowCount()
            self.tabela.insertRow(row_position)
            self.tabela.setItem(row_position, 0, QTableWidgetItem(contato.getNome()))
            self.tabela.setItem(row_position, 1, QTableWidgetItem(contato.getNumero()))
            self.tabela.setItem(row_position, 2, QTableWidgetItem(contato.getRelacao()))

    # Método pra atualizar a tabela de contatos profissionais
    def mostrar_profissionais(self):
        self.titulo_tabela.setText("Contatos profissionais:")

        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        # filtro de contatos pessoais
        pro = [c for c in contatos if isinstance(c, ContatoProfissional)] 
        # Ordem alfabética
        pro.sort(key=lambda c: c.getNome().upper())

        for contato in pro:
            row_position = self.tabela.rowCount()
            self.tabela.insertRow(row_position)
            self.tabela.setItem(row_position, 0, QTableWidgetItem(contato.getNome()))
            self.tabela.setItem(row_position, 1, QTableWidgetItem(contato.getNumero()))
            self.tabela.setItem(row_position, 2, QTableWidgetItem(contato.getEmail()))

# função que inicializa a gui
def iniciarApp():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())