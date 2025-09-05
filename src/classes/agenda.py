from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

# --- GERENCIADOR DE CONTATOS: aplica os conceitos de interação e agrupamento de objetos,
#      servindo como uma coleção centralizada para gerenciar múltiplos contatos
class Agenda:
    def __init__(self):
        self.__agenda = []

# --- MÉTODOS SEGUROS: algumas operações utilizam verificações e tratamento exceções para prevenir falhas
    def adicionarContato(self, contato):
        if not isinstance(contato, Contato):
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        
        self.__agenda.append(contato)
    
    def estaVazia(self):
        return len(self.__agenda) == 0
        
    def getAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")

        return self.__agenda

    def removerContato(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        for contato in self.__agenda:
            if contato.getNome().upper() == nome.upper():
                self.__agenda.remove(contato)
                return
        raise LookupError("Erro: Contato não encontrado para remoção.")
        
    def buscarContato(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        for contato in self.__agenda:
            if contato.getNome().upper() == nome.upper():
                return contato
        raise LookupError("Erro: Contato não encontrado para busca.")
    
    def alterarContato(self, nome, novoNome=None, novoNumero=None, novoRelacao=None, novoEmail=None):
        contato = self.buscarContato(nome)

        # ALTERA NÚMERO PRIMEIRO POR RISCO DE EXCEÇÃO
        if novoNumero and novoNumero.strip():  
            contato.setNumero(novoNumero)

        if novoNome and novoNome.strip(): 
            contato.setNome(novoNome)

        if isinstance(contato, ContatoPessoal):
            if novoRelacao and novoRelacao.strip():
                contato.setRelacao(novoRelacao)
        else: 
            if novoEmail and novoEmail.strip():
                contato.setEmail(novoEmail)

# --- VINCULAÇÃO: Python decide qual imprimir() chamar
    def imprimirAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")
        
        for contato in self.__agenda:
            if isinstance(contato, ContatoPessoal):
                contato.imprimir()
        
        for contato in self.__agenda:
            if isinstance(contato, ContatoProfissional):
                contato.imprimir()