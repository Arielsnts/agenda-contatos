from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

class Agenda:
    def __init__(self):
        self.__agenda = []

    def adicionarContato(self, contato):
        if not isinstance(contato, Contato):
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        try:
            self.__agenda.append(contato)
        except ValueError as e:
            # Captura erro específico do número e relança
            raise ValueError(f"Não foi possível adicionar o contato: {e}")
    
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

        if novoNome and novoNome.strip(): 
            contato.setNome(novoNome)

        if novoNumero and novoNumero.strip():  
            contato.__formatarNumero(novoNumero)

        if isinstance(contato, ContatoPessoal):
            if novoRelacao and novoRelacao.strip():
                contato.setRelacao(novoRelacao)
        else: 
            if novoEmail and novoEmail.strip():
                contato.setEmail(novoEmail)

    def imprimirAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")
        
        for contato in self.__agenda:
            contato.imprimir()

        for contato in self.__agenda:
            if isinstance(contato, ContatoPessoal):
                contato.imprimir()
        
        for contato in self.__agenda:
            if isinstance(contato, ContatoProfissional):
                contato.imprimir()