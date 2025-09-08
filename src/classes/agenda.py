import json
import os
from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

# --- GERENCIADOR DE CONTATOS: aplica os conceitos de interação e agrupamento de objetos,
#      servindo como uma coleção centralizada para gerenciar múltiplos contatos
class Agenda:
    def __init__(self):
        self.__agenda = []
        self.carregar()

    # --- MÉTODOS SEGUROS: algumas operações utilizam verificações e tratamento exceções para prevenir falhas
    
    # --- VERIFICAR NÚMERO DUPLICADO: Impede adicionar contatos com mesmo número
    def numeroJaExiste(self, numero):
        """Verifica se um número já existe na agenda"""
        # Formata o número para comparar no mesmo padrão
        numero_formatado = self.__formatarNumeroParaComparacao(numero)
        
        for contato in self.__agenda:
            # Desformata o número do contato para comparar apenas os dígitos
            numero_contato = ''.join(filter(str.isdigit, contato.getNumero()))
            if numero_contato == numero_formatado:
                return True
        return False

    def __formatarNumeroParaComparacao(self, numero):
        """Remove formatação do número para comparação"""
        return ''.join(filter(str.isdigit, numero))
    
    # --- ADICIONAR CONTATO: Verifica se é um objeto Contato antes de incluir e valida duplicatas
    def adicionarContato(self, contato):
        if not isinstance(contato, Contato):
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        
        # Verifica se o número já existe
        numero_limpo = ''.join(filter(str.isdigit, contato.getNumero()))
        if self.numeroJaExiste(numero_limpo):
            raise ValueError("Erro: Já existe um contato com este número.")
        
        self.__agenda.append(contato)
   
    # --- VERIFICAR SE VAZIA: Retorna True se não há contatos na agenda
    def estaVazia(self):
        return len(self.__agenda) == 0

    # --- OBTER AGENDA: Retorna a lista completa se não estiver vazia  
    def getAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")

        return self.__agenda

    # --- BUSCAR CONTATOS POR NOME: Retorna todos os contatos com o nome especificado
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

    # --- REMOVER CONTATO: Busca pelo nome e remove se encontrar (método legado - mantido para compatibilidade)
    def removerContato(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        encontrados = [c for c in self.__agenda if c.getNome().upper() == nome.upper()]
        if not encontrados:
            raise LookupError("Erro: Nenhum contato encontrado com esse nome.") 

        return encontrados
    
    # --- REMOVER CONTATO EXATO: Remove o contato específico que foi passado
    def removerContatoExato(self, contato):
        # Remove o contato exato que foi passado
        if contato in self.__agenda:
            self.__agenda.remove(contato)
        else:
            raise LookupError("Erro: Contato não encontrado para remoção.")

    # --- BUSCAR CONTATO: Encontra e retorna um contato pelo nome  
    def buscarContato(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        for contato in self.__agenda:
            if contato.getNome().upper() == nome.upper():
                return contato
        raise LookupError("Erro: Contato não encontrado para busca.")
    
    # --- ALTERAR CONTATO: Modifica os dados de um contato existente
    def alterarContato(self, nome, novoNome=None, novoNumero=None, novoRelacao=None, novoEmail=None):
        contato = self.buscarContato(nome)

        # ALTERA NÚMERO PRIMEIRO POR RISCO DE EXCEÇÃO
        if novoNumero and novoNumero.strip():  
            contato.setNumero(novoNumero)

        if novoNome and novoNome.strip(): 
            contato.setNome(novoNome)

        # Altera campo específico dependendo do tipo de contato
        if isinstance(contato, ContatoPessoal):
            if novoRelacao and novoRelacao.strip():
                contato.setRelacao(novoRelacao)
        else: 
            if novoEmail and novoEmail.strip():
                contato.setEmail(novoEmail)

    # --- ALTERAR CONTATO EXATO: Modifica os dados do contato específico que foi passado
    def alterarContatoExato(self, contato, novoNome=None, novoNumero=None, novoRelacao=None, novoEmail=None):
        # Verifica se o contato existe na agenda
        if contato not in self.__agenda:
            raise LookupError("Erro: Contato não encontrado para alteração.")

        # ALTERA NÚMERO PRIMEIRO POR RISCO DE EXCEÇÃO
        if novoNumero and novoNumero.strip():  
            contato.setNumero(novoNumero)

        if novoNome and novoNome.strip(): 
            contato.setNome(novoNome)

        # Altera campo específico dependendo do tipo de contato
        if isinstance(contato, ContatoPessoal):
            if novoRelacao and novoRelacao.strip():
                contato.setRelacao(novoRelacao)
        else: 
            if novoEmail and novoEmail.strip():
                contato.setEmail(novoEmail)

    # --- BUSCA AVANÇADA: Busca por nome, número, relação ou email
    def buscarAvancado(self, termo):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")
        
        termo_upper = termo.upper()
        encontrados = []
        
        for contato in self.__agenda:
            # Busca por nome
            if termo_upper in contato.getNome().upper():
                encontrados.append(contato)
                continue
            
            # Busca por número (remove formatação para buscar)
            numero_limpo = contato.getNumero().replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
            if termo in numero_limpo:
                encontrados.append(contato)
                continue
            
            # Busca específica por tipo
            if isinstance(contato, ContatoPessoal):
                if termo_upper in contato.getRelacao().upper():
                    encontrados.append(contato)
            elif isinstance(contato, ContatoProfissional):
                if termo_upper in contato.getEmail().upper():
                    encontrados.append(contato)
        
        if not encontrados:
            raise LookupError("Erro: Nenhum contato encontrado com esse termo de busca.")
        
        return encontrados

    # --- IMPRIMIR AGENDA: Mostra todos os contatos separados por tipo
    def imprimirAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")
        
        # Primeiro os contatos pessoais
        for contato in self.__agenda:
            if isinstance(contato, ContatoPessoal):
                contato.imprimir()
        
        # Depois os contatos profissionais
        for contato in self.__agenda:
            if isinstance(contato, ContatoProfissional):
                contato.imprimir()

    # --- json
    # --- SALVAR AGENDA: Grava todos os contatos em arquivo JSON para persistência
    def salvar(self, caminho="src/data/contatos.json"):
        dados = [contato.to_dict() for contato in self.__agenda]

        os.makedirs(os.path.dirname(caminho), exist_ok=True)

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    # --- CARREGAR AGENDA: Recupera contatos salvos no arquivo JSON ao iniciar
    def carregar(self, caminho="src/data/contatos.json"):
        if not os.path.exists(caminho):
            return  # nada pra carregar ainda

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            dados = [] 

        self.__agenda.clear()
        for item in dados:
            tipo = item.get("tipo")
            if tipo == "pessoal":
                self.__agenda.append(ContatoPessoal.from_dict(item))
            elif tipo == "profissional":
                self.__agenda.append(ContatoProfissional.from_dict(item))