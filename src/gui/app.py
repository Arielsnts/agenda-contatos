import sys # Necessário para rodar a aplicação PyQt5

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QLabel, QHeaderView, QHBoxLayout
)

from PyQt5.QtCore import Qt # Para alinhamento e outras constantes
from PyQt5.QtWidgets import QListWidget # Para listas de seleção
from functools import partial # Para passar argumentos em slots

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

        # Estilo padrão dos botões
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

        # widgets auxiliares para remoção múltipla
        self.lista_remocao = QListWidget()
        self.confirmar_remover_button = QPushButton("Remover Selecionado")
        self.confirmar_remover_button.setStyleSheet(self.botao_style)
        self.confirmar_remover_button.clicked.connect(self.remover_selecionado)

        # widgets auxiliares para alteração múltipla
        self.lista_alteracao = QListWidget()
        self.confirmar_alterar_button = QPushButton("Alterar Selecionado")
        self.confirmar_alterar_button.setStyleSheet(self.botao_style)
        self.confirmar_alterar_button.clicked.connect(self.alterar_selecionado)
        self._dados_alteracao = {}

        # --- DEBUG: Adicionando contatos iniciais
        # self.__agenda.adicionarContato(ContatoPessoal("Ariel", "79991234567", "Amigo"))

        # --- WIDGETS COMUNS
        self.texto_form = QLabel("")
        self.texto_form.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.erro = QLabel("")
        self.erro.setStyleSheet("color: red; font-weight: bold")

        self.volta_button = QPushButton("Voltar pro menu")
        self.volta_button.setStyleSheet(self.botao_style)
        self.volta_button.clicked.connect(self.voltar_menu)

        # ----- WIDGETS/LAYOUTS DE CONTAINER SUPERIOR

        # --- MENU
        self.texto_menu = QLabel("Agenda de Contatos")
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

        # NOVO: Botão de busca
        self.buscar_button = QPushButton("Buscar Contato")
        self.buscar_button.setStyleSheet(self.botao_style)
        self.buscar_button.clicked.connect(self.mostrar_busca)

        # --- WIDGETS DE BUSCA
        self.campo_busca = QLineEdit()
        self.campo_busca.setPlaceholderText("Digite nome, número, relação ou email...")
        
        self.submit_busca = QPushButton("Buscar")
        self.submit_busca.setStyleSheet(self.botao_style)
        self.submit_busca.clicked.connect(self.realizar_busca)

        # --- LAYOUT DE MENU INICIAL
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.texto_menu)
        menu_layout.addWidget(self.add_button)
        menu_layout.addWidget(self.remover_button)
        menu_layout.addWidget(self.alterar_button)
        menu_layout.addWidget(self.buscar_button)
        menu_layout.addWidget(self.erro)

        # --- RESTO DOS WIDGETS (adicionar todos os outros campos de formulário...)
        # Pessoais
        self.nome_pessoal_add = QLineEdit()
        self.numero_pessoal_add = QLineEdit()
        self.relacao_pessoal_add = QLineEdit()
        self.submit_pessoal = QPushButton("Adicionar contato")
        self.submit_pessoal.setStyleSheet(self.botao_style)
        self.submit_pessoal.clicked.connect(self.click_adicionar_pessoal)

        # Profissionais
        self.nome_pro_add = QLineEdit()
        self.numero_pro_add = QLineEdit()
        self.email_pro_add = QLineEdit()
        self.submit_pro = QPushButton("Adicionar contato")
        self.submit_pro.setStyleSheet(self.botao_style)
        self.submit_pro.clicked.connect(self.click_adicionar_pro)

        # Remover
        self.nome_remover = QLineEdit()
        self.submit_remover = QPushButton("Remover contato")
        self.submit_remover.setStyleSheet(self.botao_style)
        self.submit_remover.clicked.connect(self.click_remover)

        # Alterar
        self.nome_alterar = QLineEdit()
        self.novo_nome = QLineEdit()
        self.novo_numero = QLineEdit()
        self.novo_relacao = QLineEdit()
        self.novo_email = QLineEdit()
        self.submit_alterar = QPushButton("Alterar contato")
        self.submit_alterar.setStyleSheet(self.botao_style)
        self.submit_alterar.clicked.connect(self.click_alterar)

        # --- CONTAINER SUPERIOR
        self.container_superior = QWidget()
        self.container_superior.setLayout(menu_layout)

        # -------- WIDGETS/LAYOUTS DE CONTAINER INFERIOR
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
        texto.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(texto)

        pessoal_button = QPushButton("Pessoal")
        pessoal_button.setStyleSheet(self.botao_style)
        pessoal_button.clicked.connect(self.mostrar_adicionar_pessoal)

        pro_button = QPushButton("Profissional")
        pro_button.setStyleSheet(self.botao_style)
        pro_button.clicked.connect(self.mostrar_adicionar_pro)

        layout.addWidget(pessoal_button)
        layout.addWidget(pro_button)
        layout.addWidget(self.volta_button)

    #   Metódo que alterna para o form de adicionar contato pessoal
    def mostrar_adicionar_pessoal(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        # Adiciona os widgets do formulário no mesmo layout
        layout.addWidget(self.texto_form)
        self.texto_form.setText("Preencha para adicionar um contato pessoal: ")

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
        self.texto_form.setText("Preencha para adicionar um contato profissional: ")

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
        self.texto_form.setText("Preencha para remover a primeira aparição de um contato: ")

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
        texto = QLabel("Preencha para alterar a primeira aparição (Campos vazios não serão alterados):")
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

    # Método para mostrar formulário de busca
    def mostrar_busca(self):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)
        
        layout.addWidget(QLabel("Busca Avançada:"))
        layout.addWidget(QLabel("Digite qualquer termo (nome, número, relação ou email):"))
        layout.addWidget(self.campo_busca)
        layout.addWidget(self.submit_busca)
        layout.addWidget(self.volta_button)
        layout.addWidget(self.erro)

    # Método para realizar busca
    def realizar_busca(self):
        termo = self.campo_busca.text()
        
        if not termo:
            self.erro.setText("Erro: Digite um termo para buscar.")
            return
        
        self.erro.clear()
        
        try:
            encontrados = self.__agenda.buscarAvancado(termo)
            self.mostrar_resultados_busca(encontrados, termo)
        except LookupError as e:
            self.erro.setText(str(e))

    # Método para mostrar resultados da busca
    def mostrar_resultados_busca(self, contatos, termo):
        self.titulo_tabela.setText(f"Resultados da busca por '{termo}' ({len(contatos)} encontrado(s)):")
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
        
        self.campo_busca.clear()
        self.voltar_menu()

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

    # Método que altera um contato único
    def alterar_contato_unico(self, contato):
        nome = self._dados_alteracao['nome']
        numero = self._dados_alteracao['numero']
        relacao = self._dados_alteracao['relacao']
        email = self._dados_alteracao['email']

        try:
            # ALTERA NÚMERO PRIMEIRO POR RISCO DE EXCEÇÃO
            if numero and numero.strip():  
                contato.setNumero(numero)

            if nome and nome.strip(): 
                contato.setNome(nome)

            # Altera campo específico dependendo do tipo de contato
            if isinstance(contato, ContatoPessoal):  # <-- MUDANÇA AQUI
                if relacao and relacao.strip():
                    contato.setRelacao(relacao)
                    print(f"DEBUG: Relação alterada para '{relacao}'")  # DEBUG
            elif isinstance(contato, ContatoProfissional):  # <-- MUDANÇA AQUI
                if email and email.strip():
                    contato.setEmail(email)
                    print(f"DEBUG: Email alterado para '{email}'")  # DEBUG
                    
        except ValueError as e:
            self.erro.setText(str(e))
            return
        
        print(f"Contato {contato.getNome()} alterado com sucesso.")
        self.__agenda.salvar()
        self.limpar_campos_alteracao()
        self.voltar_menu()
        self.mostrar_pessoais()

    # Método para o botão alterar (modificado)
    def click_alterar(self):
        nome_alterar = self.nome_alterar.text()

        if not nome_alterar:
            self.erro.setText("Erro: Preencha pelo menos o campo nome para buscar.")
            return

        self.erro.clear()

        # Salva os dados dos campos para usar depois
        self._dados_alteracao = {
            'nome': self.novo_nome.text(),
            'numero': self.novo_numero.text(),
            'relacao': self.novo_relacao.text(),
            'email': self.novo_email.text()
        }

        try:
            # Usa o mesmo método que a remoção usa
            encontrados = self.__agenda.buscarContatosPorNome(nome_alterar)
        except LookupError as e:
            self.erro.setText(str(e))
            return
        
        print(f"Encontrados {len(encontrados)} contatos com o nome '{nome_alterar}'")  # DEBUG
        
        # Se encontrou apenas um contato, altera diretamente
        if len(encontrados) == 1:
            self.alterar_contato_unico(encontrados[0])
        else:
            # Se encontrou múltiplos, mostra lista de opções
            self.mostrar_opcoes_alteracao(encontrados)

    # Método para o botão de adicionar pessoal
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

        if not nome or not numero or not email:
            self.erro.setText("Erro: Preencha todos os campos.")
            return

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
            encontrados = self.__agenda.buscarContatosPorNome(nome)
        except LookupError as e:
            self.erro.setText(str(e))
            # DEBUG
            # print(e)
            return
        
        # DEBUG
        print(f"Contato {nome} removido.")

        self.__agenda.salvar()

        if len(encontrados) == 1:
            self.__agenda.removerContatoExato(encontrados[0])
            self.nome_remover.clear()
            self.voltar_menu()
            self.mostrar_pessoais()
        else:
            # mostrar lista de opções
            self.mostrar_opcoes_remocao(encontrados)

    # --- MÉTODOS PARA ATUALIZAÇÃO DA TABELA

    # Método que mostra opções de alteração quando há mais de um contato com o mesmo nome
    def mostrar_opcoes_alteracao(self, contatos):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(QLabel("Foram encontrados vários contatos com esse nome. Escolha qual alterar:"))

        self.lista_alteracao.clear()
        self._contatos_para_alterar = contatos  # guarda os objetos internamente

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

    # Função que altera o contato selecionado na lista
    def alterar_selecionado(self):
        selected_row = self.lista_alteracao.currentRow()
        if selected_row == -1:
            self.erro.setText("Erro: Selecione um contato para alterar.")
            return

        contato = self._contatos_para_alterar[selected_row]
        self.alterar_contato_unico(contato)

    # Método para limpar os campos de alteração
    def limpar_campos_alteracao(self):
        self.nome_alterar.clear()
        self.novo_nome.clear()
        self.novo_numero.clear()
        self.novo_relacao.clear()
        self.novo_email.clear()

    # ----- MÉTODO PARA A CLASSE AGENDA -----

    # Adicione este método na classe Agenda:
    def buscarContatosPorNome(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        encontrados = []
        for contato in self.__agenda:
            if contato.getNome().upper() == nome.upper():
                encontrados.append(contato)
        
        if not encontrados:
            raise LookupError("Erro: Contato não encontrado.")
        
        return encontrados
    
    # Método que mostra opções de remoção quando há mais de um contato com o mesmo nome
    def mostrar_opcoes_remocao(self, contatos):
        layout = self.container_superior.layout()
        self.limpar_layout(layout)

        layout.addWidget(QLabel("Foram encontrados vários contatos com esse nome. Escolha um:"))

        self.lista_remocao.clear()
        self._contatos_para_remover = contatos  # guarda os objetos internamente

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

    # função que remove o contato selecionado na lista
    def remover_selecionado(self):
        selected_row = self.lista_remocao.currentRow()
        if selected_row == -1:
            self.erro.setText("Erro: Selecione um contato para remover.")
            return

        contato = self._contatos_para_remover[selected_row]
        self.__agenda.removerContatoExato(contato)

        self.nome_remover.clear()
        self.voltar_menu()
        self.mostrar_pessoais()
         

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

        for c in pessoais:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getRelacao()))

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

        for c in pro:
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(c.getNome()))
            self.tabela.setItem(row, 1, QTableWidgetItem(c.getNumero()))
            self.tabela.setItem(row, 2, QTableWidgetItem(c.getEmail()))

    # Método pra mostrar a tabela com todos os contatos
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
