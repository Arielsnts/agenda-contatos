import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QLabel, QHeaderView, QHBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtGui import QIcon

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
        self.setWindowIcon(QIcon("src/gui/agenda.png"))

        # Objeto agenda (lista de Contato)
        self.__agenda = Agenda()

        # --- DEBUG: Adicionando contatos iniciais
        # self.__agenda.adicionarContato(ContatoPessoal("Ariel", "79991234567", "Amigo"))

        # ----- ESTILOS
        self.setStyleSheet("background-color: #606B73; color: #FFFFFF; font-family: 'Ubuntu', Arial;")

        self.texto_style = """
            font-size: 18px;
            font-weight: bold;
            color: #FFFFFF;
            font-family: 'Ubuntu', Arial;
        """

        self.botao_style = """
        QPushButton {
            background-color: #FFFFFF;
            color: #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 14px;
            min-width: 200px;
            font-family: 'Ubuntu', Arial;
        }
        QPushButton:hover {
            background-color: #A69F95;
            color: #293133;
        }
        """

        self.input_style = """
        QLineEdit {
            background-color: #FFFFFF;
            color: #000000;
            border: 2px solid #A69F95;
            border-radius: 5px;
            padding: 3px;
            font-size: 14px;
            font-family: 'Ubuntu', Arial;
        }
        """

        # ----- WIDGETS COMUNS

        self.texto_form = QLabel("")
        self.texto_form.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.erro = QLabel("")
        self.erro.setStyleSheet("font-size: 20px; color: #F55B5B; font-weight: bold;")

        self.volta_button = QPushButton("Voltar pro menu")
        self.volta_button.setStyleSheet(self.botao_style)
        self.volta_button.setCursor(Qt.PointingHandCursor)
        self.volta_button.clicked.connect(self.voltar_menu)

        # ----- WIDGETS/LAYOUTS DE CONTAINER SUPERIOR

        # --- MENU

        self.texto_menu = QLabel("Escolha uma opção:")
        self.texto_menu.setStyleSheet(self.texto_style)
        self.texto_menu.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.add_button = QPushButton("Adicionar Contato")
        self.add_button.setStyleSheet(self.botao_style)
        self.add_button.setCursor(Qt.PointingHandCursor)
        self.add_button.clicked.connect(self.mostrar_menu_add)

        self.remover_button = QPushButton("Remover Contato")
        self.remover_button.setStyleSheet(self.botao_style)
        self.remover_button.setCursor(Qt.PointingHandCursor)
        self.remover_button.clicked.connect(self.mostrar_remover)

        self.alterar_button = QPushButton("Alterar Contato")
        self.alterar_button.setStyleSheet(self.botao_style)
        self.alterar_button.setCursor(Qt.PointingHandCursor)
        self.alterar_button.clicked.connect(self.mostrar_alterar)

        self.buscar_button = QPushButton("Buscar Contato")
        self.buscar_button.setStyleSheet(self.botao_style)
        self.buscar_button.setCursor(Qt.PointingHandCursor)
        self.buscar_button.clicked.connect(self.mostrar_busca)

        # - LAYOUT DE MENU INICIAL
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.texto_menu)
        menu_layout.addWidget(self.add_button)
        menu_layout.addWidget(self.remover_button)
        menu_layout.addWidget(self.buscar_button)
        menu_layout.addWidget(self.alterar_button)
        menu_layout.addWidget(self.erro)

        # --- ADICIONAR PESSOAL

        self.nome_pessoal_add = QLineEdit()
        self.nome_pessoal_add.setStyleSheet(self.input_style)

        self.numero_pessoal_add = QLineEdit()
        self.numero_pessoal_add.setStyleSheet(self.input_style)

        self.relacao_pessoal_add = QLineEdit()
        self.relacao_pessoal_add.setStyleSheet(self.input_style)

        self.submit_pessoal = QPushButton("Adicionar contato")
        self.submit_pessoal.setStyleSheet(self.botao_style)
        self.submit_pessoal.setCursor(Qt.PointingHandCursor)
        self.submit_pessoal.clicked.connect(self.click_adicionar_pessoal)

        # --- ADICIONAR PROFISSIONAL

        self.nome_pro_add = QLineEdit()
        self.nome_pro_add.setStyleSheet(self.input_style)

        self.numero_pro_add = QLineEdit()
        self.numero_pro_add.setStyleSheet(self.input_style)
        
        self.email_pro_add = QLineEdit()
        self.email_pro_add.setStyleSheet(self.input_style)
        
        self.submit_pro = QPushButton("Adicionar contato")
        self.submit_pro.setStyleSheet(self.botao_style)
        self.submit_pro.setCursor(Qt.PointingHandCursor)
        self.submit_pro.clicked.connect(self.click_adicionar_pro)

        # --- REMOVER CONTATO

        self.nome_remover = QLineEdit()
        self.nome_remover.setStyleSheet(self.input_style)

        self.submit_remover = QPushButton("Remover contato")
        self.submit_remover.setStyleSheet(self.botao_style)
        self.submit_remover.setCursor(Qt.PointingHandCursor)
        self.submit_remover.clicked.connect(self.click_remover)

        # - REMOÇÃO MÚLTIPLA

        self.lista_remocao = QListWidget()
        
        self.confirmar_remover_button = QPushButton("Remover Selecionado")
        self.confirmar_remover_button.setStyleSheet(self.botao_style)
        self.confirmar_remover_button.setCursor(Qt.PointingHandCursor)
        self.confirmar_remover_button.clicked.connect(self.click_remover_selecionado)

        # --- BUSCAR CONTATO
        
        self.campo_busca = QLineEdit()
        self.campo_busca.setStyleSheet(self.input_style)
        
        self.submit_busca = QPushButton("Buscar")
        self.submit_busca.setStyleSheet(self.botao_style)
        self.submit_busca.setCursor(Qt.PointingHandCursor)
        self.submit_busca.clicked.connect(self.click_buscar)

        # --- ALTERAR CONTATO

        self.nome_alterar = QLineEdit()
        self.nome_alterar.setStyleSheet(self.input_style)
        
        self.novo_nome = QLineEdit()
        self.novo_nome.setStyleSheet(self.input_style)

        self.novo_numero = QLineEdit()
        self.novo_numero.setStyleSheet(self.input_style)
        
        self.novo_relacao = QLineEdit()
        self.novo_relacao.setStyleSheet(self.input_style)
        
        self.novo_email = QLineEdit()
        self.novo_email.setStyleSheet(self.input_style)
        
        self.submit_alterar = QPushButton("Alterar contato")
        self.submit_alterar.setStyleSheet(self.botao_style)
        self.submit_alterar.setCursor(Qt.PointingHandCursor)
        self.submit_alterar.clicked.connect(self.click_alterar)

        # - ALTERAÇÃO MÚLTIPLA

        self.lista_alteracao = QListWidget()
        
        self.confirmar_alterar_button = QPushButton("Alterar Selecionado")
        self.confirmar_alterar_button.setStyleSheet(self.botao_style)
        self.confirmar_alterar_button.setCursor(Qt.PointingHandCursor)
        self.confirmar_alterar_button.clicked.connect(self.click_alterar_selecionado)
        
        self._dados_alteracao = {}

        # --- CONTAINER SUPERIOR
        
        self.container_superior = QWidget()
        self.container_superior.setLayout(menu_layout)

        # ------ WIDGETS/LAYOUTS DE CONTAINER INFERIOR

        # --- BOTÕES

        self.pessoal_view_button = QPushButton("Visualizar contatos pessoais")
        self.pessoal_view_button.setStyleSheet(self.botao_style)
        self.pessoal_view_button.setCursor(Qt.PointingHandCursor)
        self.pessoal_view_button.clicked.connect(self.mostrar_pessoais)

        self.pro_view_button = QPushButton("Visualizar contatos profissionais")
        self.pro_view_button.setStyleSheet(self.botao_style)
        self.pro_view_button.setCursor(Qt.PointingHandCursor)
        self.pro_view_button.clicked.connect(self.mostrar_profissionais)

        self.todos_view_button = QPushButton("Visualizar todos os contatos")
        self.todos_view_button.setStyleSheet(self.botao_style)
        self.todos_view_button.setCursor(Qt.PointingHandCursor)
        self.todos_view_button.clicked.connect(self.mostrar_todos)

        # --- LAYOUT DOS BOTÕES

        button_out_layout = QHBoxLayout()
        button_out_layout.addWidget(self.pessoal_view_button)
        button_out_layout.addWidget(self.pro_view_button)
        button_out_layout.addWidget(self.todos_view_button)

        # --- TABELA

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Número", "Relação/Email"])

        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        self.tabela.setColumnWidth(0, 270)
        self.tabela.setColumnWidth(1, 270)
        self.tabela.setColumnWidth(2, 400)

        self.tabela.setStyleSheet("font-size: 14px;")

        self.titulo_tabela = QLabel("Contatos pessoais:")
        self.titulo_tabela.setStyleSheet(self.texto_style)

        self.mostrar_pessoais()

        # --- LAYOUT INFERIOR

        inferior_layout = QVBoxLayout()
        inferior_layout.addLayout(button_out_layout)
        inferior_layout.addWidget(self.titulo_tabela)
        inferior_layout.addWidget(self.tabela)

        # --- CONTAINER INFERIOR

        self.container_inferior = QWidget()
        self.container_inferior.setLayout(inferior_layout)

        # ----- PRINCIPAL

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.container_superior)
        main_layout.addWidget(self.container_inferior)

        container_main = QWidget()
        container_main.setLayout(main_layout)
        self.setCentralWidget(container_main)

    # ----- MÉTODOS

    # --- MÉTODOS DE ALTERAÇÃO DE TELA

    # Método que limpa widgets e layouts internos
    def limpar_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            # Se for widget, remove do parent
            widget = item.widget()
            if widget: widget.setParent(None)

            # Se for um layout interno, limpa recursivamente
            elif item.layout(): self.limpar_layout(item.layout())

    # Metódo que alterna para o form de adicionar contato pessoal
    def mostrar_menu_add(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do menu de adicionar contato
        texto = QLabel("Escolha o tipo de contato:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

        pessoal_button = QPushButton("Pessoal")
        pessoal_button.setStyleSheet(self.botao_style)
        pessoal_button.setCursor(Qt.PointingHandCursor)
        pessoal_button.clicked.connect(self.mostrar_adicionar_pessoal)

        pro_button = QPushButton("Profissional")
        pro_button.setStyleSheet(self.botao_style)
        pro_button.setCursor(Qt.PointingHandCursor)
        pro_button.clicked.connect(self.mostrar_adicionar_pro)

        layout.addWidget(pessoal_button)
        layout.addWidget(pro_button)
        layout.addWidget(self.volta_button)

    # Metódo que alterna para o form de adicionar contato pessoal
    def mostrar_adicionar_pessoal(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        texto = QLabel("Preencha para adicionar contato pessoal:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

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
        texto = QLabel("Preencha para adicionar contato profissional:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

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
        texto = QLabel("Preencha para remover um contato:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

        layout.addWidget(QLabel("Nome do contato para ser removido:"))
        layout.addWidget(self.nome_remover)

        layout.addWidget(self.submit_remover)

        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    # Método que mostra opções de remoção quando há mais de um contato com o mesmo nome
    def mostrar_opcoes_remover(self, contatos):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        texto = QLabel("Selecione qual contato será removido:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

        self.lista_remocao.clear()

        # Lista de contatos para remover. Será usada pelo método click_remover_selecionado()
        self._contatos_para_remover = contatos

        for contato in contatos:
            if isinstance(contato, ContatoPessoal):
                info = f"{contato.getNome()} - {contato.getNumero()} - {contato.getRelacao()}"
            else:
                info = f"{contato.getNome()} - {contato.getNumero()} - {contato.getEmail()}"
            self.lista_remocao.addItem(info)

        layout.addWidget(self.lista_remocao)
        layout.addWidget(self.confirmar_remover_button)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    # Método para mostrar formulário de busca
    def mostrar_busca(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)
        
        texto = QLabel("Preencha para buscar um contato:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

        layout.addWidget(QLabel("Nome do termo para busca (nome, número, relação ou email):"))

        layout.addWidget(self.campo_busca)
        layout.addWidget(self.submit_busca)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    # Metódo que alterna para o form de alterar contato
    def mostrar_alterar(self):
        layout = self.container_superior.layout()

        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        texto = QLabel("Preencha para alterar um contato (campos vazio não serão alterados):")
        texto.setStyleSheet(self.texto_style)
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

    # Método que mostra opções de alteração quando há mais de um contato com o mesmo nome
    def mostrar_opcoes_alteracao(self, contatos):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        texto = QLabel("Selecione qual contato será alterado:")
        texto.setStyleSheet(self.texto_style)
        layout.addWidget(texto)

        self.lista_alteracao.clear()

        # Lista de contatos para alterar. Será usada pelo método click_alterar_selecionado()
        self._contatos_para_alterar = contatos

        # Constrói a lista de contatos para selecionar
        for contato in contatos:
            if isinstance(contato, ContatoPessoal):
                info = f"{contato.getNome()} - {contato.getNumero()} - {contato.getRelacao()}"
            else:
                info = f"{contato.getNome()} - {contato.getNumero()} - {contato.getEmail()}"
            self.lista_alteracao.addItem(info)

        layout.addWidget(self.lista_alteracao)
        layout.addWidget(self.confirmar_alterar_button)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    # Método que retorna para o menu de opções
    def voltar_menu(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(self.texto_menu)

        layout.addWidget(self.add_button)

        layout.addWidget(self.remover_button)
        
        layout.addWidget(self.buscar_button)  

        layout.addWidget(self.alterar_button)

        self.erro.clear()

    # --- MÉTODOS PARA O FUNCIONAMENTO DOS BOTÕES

    # Método para o botão de adicionar pessoal
    def click_adicionar_pessoal(self):
        nome = self.nome_pessoal_add.text()
        numero = self.numero_pessoal_add.text()
        relacao = self.relacao_pessoal_add.text()

        self.erro.clear()

        try:
            self.__agenda.adicionarContato(ContatoPessoal(nome, numero, relacao))
        except ValueError as e:
            self.erro.setText(str(e))
            # DEBUG
            # print(e)
            return
        
        # DEBUG
        print(f"Contato pessoal {nome} adicionado.")

        self.__agenda.salvar()

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

        self.erro.clear()

        try:
            self.__agenda.adicionarContato(ContatoProfissional(nome, numero, email))
        except ValueError as e:
            self.erro.setText(str(e))
            # DEBUG
            # print(e)
            return
        
        # DEBUG
        print(f"Contato profissional {nome} adicionado.")

        self.__agenda.salvar()

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
            encontrados = self.__agenda.buscarContato(nome)
        except LookupError as e:
            self.erro.setText(str(e))
            # DEBUG
            # print(e)
            return

        if len(encontrados) == 1:
            self.__agenda.removerContato(encontrados[0])

            self.__agenda.salvar()

            self.nome_remover.clear()

            self.voltar_menu()
            self.mostrar_pessoais()

            # DEBUG
            print(f"Contato {nome} removido.")
        else:
            self.mostrar_opcoes_remover(encontrados)

    # Método que remove o contato selecionado na lista
    def click_remover_selecionado(self):
        selecionado = self.lista_remocao.currentRow()

        if selecionado == -1:
            self.erro.setText("Erro: Selecione um contato para remover.")
            return

        contato = self._contatos_para_remover[selecionado]

        self.__agenda.removerContato(contato)

        self.__agenda.salvar()

        self.nome_remover.clear()
        self.voltar_menu()
        self.mostrar_pessoais()

    # Método para realizar busca
    def click_buscar(self):
        termo = self.campo_busca.text()
        
        if not termo:
            self.erro.setText("Erro: Digite um termo para buscar.")
            return
        
        self.erro.clear()
        
        try:
            encontrados = self.__agenda.buscarContato(termo)
            self.mostrar_resultados_busca(encontrados, termo)
        except LookupError as e:
            self.erro.setText(str(e))

        self.campo_busca.clear()
        self.voltar_menu()

    # Método para o botão alterar
    def click_alterar(self):
        self.nome_alterar_metodo = self.nome_alterar.text()

        if not self.nome_alterar_metodo:
            self.erro.setText("Erro: Preencha pelo menos o campo nome para buscar.")
            return
        
        self.nome_novo = self.novo_nome.text()
        self.numero_novo = self.novo_numero.text()
        self.relacao_novo = self.novo_relacao.text()
        self.email_novo = self.novo_email.text()


        if self.numero_novo.strip():
            if len(self.numero_novo) != 11:
                self.erro.setText("Erro: O número deve conter exatamente 11 dígitos.")
                return

            if self.numero_novo[2] != "9":
                self.erro.setText("Erro: O número deve começar com 9 após o DDD.")
                return

            if self.__agenda.numeroJaExiste(self.numero_novo):
                self.erro.setText("Erro: Já existe um contato com esse número.")
                return

        self.erro.clear()

        self.nome_alterar.clear()
        self.novo_nome.clear()
        self.novo_numero.clear()
        self.novo_relacao.clear()
        self.novo_email.clear()

        try:
            encontrados = self.__agenda.buscarContato(self.nome_alterar_metodo)
        except LookupError as e:
            self.erro.setText(str(e))
            return
        
        if len(encontrados) == 1:
            try:
                self.__agenda.alterarContato(
                    encontrados[0], 
                    self.nome_novo, 
                    self.numero_novo, 
                    self.relacao_novo, 
                    self.email_novo
                )
            except ValueError as e:
                self.erro.setText(str(e))
                return
            
            # DEBUG
            print(f"O contato {encontrados[0].getNome()} foi alterado.")

            self.__agenda.salvar()

            self.voltar_menu()
            self.mostrar_pessoais()

        else:
            self.mostrar_opcoes_alteracao(encontrados)

    # Método para alterar contato selecionado 
    def click_alterar_selecionado(self):
        selecionado = self.lista_alteracao.currentRow()

        if selecionado == -1:
            self.erro.setText("Erro: Selecione um contato para alterar.")
            return

        contato_selecionado = self._contatos_para_alterar[selecionado]

        try:
            self.__agenda.alterarContato(
                contato_selecionado,
                self.nome_novo,
                self.numero_novo,
                self.relacao_novo,
                self.email_novo
            )
        except ValueError as e:
            self.erro.setText(str(e))
            return

        # DEBUG
        print(f"O contato {contato_selecionado.getNome()} foi alterado.")

        self.__agenda.salvar()

        self.voltar_menu()
        self.mostrar_pessoais()

    # --- MÉTODOS PARA ATUALIZAÇÃO DA TABELA         

    # Método pra atualizar a tabela de contatos pessoais
    def mostrar_pessoais(self):
        self.titulo_tabela.setText("Contatos pessoais:")
        self.titulo_tabela.setStyleSheet(self.texto_style)
        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        # filtro de contatos pessoais
        pessoais = [c for c in contatos if isinstance(c, ContatoPessoal)]
        # Ordem alfabética
        pessoais.sort(key=lambda c: c.getNome().upper())

        for c in pessoais:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getRelacao()))

    # Método pra atualizar a tabela de contatos profissionais
    def mostrar_profissionais(self):
        self.titulo_tabela.setText("Contatos profissionais:")
        self.titulo_tabela.setStyleSheet(self.texto_style)
        self.tabela.setRowCount(0)

        try:
            contatos = self.__agenda.getAgenda()
        except ValueError:
            contatos = []

        # filtro de contatos pessoais
        pro = [c for c in contatos if isinstance(c, ContatoProfissional)]
        # Ordem alfabética
        pro.sort(key=lambda c: c.getNome().upper())

        for c in pro:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getEmail()))

    # Método pra mostrar a tabela com todos os contatos
    def mostrar_todos(self):
        self.titulo_tabela.setText("Todos os contatos:")
        self.titulo_tabela.setStyleSheet(self.texto_style)
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

    # Método para mostrar resultados da busca
    def mostrar_resultados_busca(self, contatos, termo):
        self.titulo_tabela.setText(f"Resultados da busca por '{termo}' ({len(contatos)} encontrado(s)):")
        self.titulo_tabela.setStyleSheet(self.texto_style)
        self.tabela.setRowCount(0)
        
        # Ordena por nome
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

    # Método de encerramento
    def closeEvent(self, event):
        print("Aplicação encerrada.")
        event.accept() 

# função que inicializa a gui
def iniciarApp():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    print("Aplicação inicializada.")
    sys.exit(app.exec_())
