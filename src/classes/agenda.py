from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

# --- GERENCIADOR DE CONTATOS: aplica os conceitos de interação e agrupamento de objetos,
#      servindo como uma coleção centralizada para gerenciar múltiplos contatos
class Agenda:
    def __init__(self):
        self.__agenda = []

    # --- MÉTODOS SEGUROS: algumas operações utilizam verificações e tratamento exceções para prevenir falhas
    # --- ADICIONAR CONTATO: Verifica se é um objeto Contato antes de incluir
    def adicionarContato(self, contato):
        if not isinstance(contato, Contato):
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        
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

        encontrados = [c for c in self.__agenda if c.getNome().upper() == nome.upper()]
        if not encontrados:
            raise LookupError("Erro: Nenhum contato encontrado com esse nome.")

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

    # --- VINCULAÇÃO: Python decide qual imprimir() chamar
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