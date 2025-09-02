from contato.contato import Contato
from contato.contato_pessoal import ContatoPessoal
from contato.contato_profissional import ContatoProfissional


class Catalogo:
    def __init__(self):
        self.__agenda = []

    def Adicionar_Contato(self, contato):
        if isinstance(contato, Contato):
            self.__agenda.append(contato)

        else:
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        

    def Remover_Contato(self, contato):
        if contato in  self.__agenda:
            self.__agenda.remove(contato)

        else:
            raise TypeError("Erro: esse contato não esta na agenda.")
        
    def Buscar_Contato(self, contato):
        for i in self.__agenda:
            if i.getNome() == contato:
                return i.imprime()
        print("Contato não encontrado.")

