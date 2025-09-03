from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

class Agenda:
    def __init__(self):
        self.__agenda = []

    def adicionarContato(self, contato):
        if isinstance(contato, Contato):
            self.__agenda.append(contato)
        else:
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        
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

    def imprimirAgenda(self):
        if self.estaVazia():
            raise ValueError("Erro: A lista está vazia.")

        for contato in self.__agenda:
            if isinstance(contato, ContatoPessoal):
                contato.imprimir()
        
        for contato in self.__agenda:
            if isinstance(contato, ContatoProfissional):
                contato.imprimir()