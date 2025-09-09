import json
import os
from classes.contato import Contato
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

# --- GERENCIADOR DE CONTATOS: aplica os conceitos de interação e agrupamento de objetos,
# servindo como uma coleção centralizada para gerenciar múltiplos contatos
class Agenda:
    def __init__(self):
        self.__agenda = []
        self.carregar()

    # --- ADICIONAR CONTATO: Verifica se é um objeto Contato antes de incluir e valida duplicatas
    def adicionarContato(self, contato):
        if not isinstance(contato, Contato):
            raise TypeError("Erro: só é permitido adicionar objetos do tipo Contato.")
        
        if self.__numeroJaExiste(contato.getNumero()):
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
    
    # --- MÉTODOS SEGUROS: algumas operações utilizam verificações e tratamento exceções para prevenir falhas
    # --- VERIFICAR NÚMERO DUPLICADO: Impede adicionar contatos com mesmo número
    def __numeroJaExiste(self, numero):
        numero_desformatado = self.__desformatarNumero(numero)
        
        for contato in self.__agenda:
            numero_contato = self.__desformatarNumero(contato.getNumero())

            if numero_contato == numero_desformatado:
                return True
            
        return False

    def __desformatarNumero(self, numero):
        return ''.join(filter(str.isdigit, numero))

    # --- BUSCAR CONTATOS POR NOME: Retorna todos os contatos com o nome especificado
    def buscarContatos(self, nome):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")

        encontrados = []
        for contato in self.__agenda:
            if contato.getNome().upper() == nome.upper():
                encontrados.append(contato)
        
        if not encontrados:
            raise LookupError("Erro: Contato não encontrado.")
        
        return encontrados
    
    # --- BUSCA AVANÇADA: Busca por nome, número, relação ou email
    def buscarAvancado(self, termo):
        if self.estaVazia():
            raise LookupError("Erro: A lista está vazia.")
        
        termo_upper = termo.upper()
        encontrados = []
        
        for contato in self.__agenda:
            if termo_upper in contato.getNome().upper():
                encontrados.append(contato)
                continue
            
            numero_limpo = contato.getNumero().replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
            if termo in numero_limpo:
                encontrados.append(contato)
                continue
            
            if isinstance(contato, ContatoPessoal):
                if termo_upper in contato.getRelacao().upper():
                    encontrados.append(contato)
            elif isinstance(contato, ContatoProfissional):
                if termo_upper in contato.getEmail().upper():
                    encontrados.append(contato)
        
        if not encontrados:
            raise LookupError("Erro: Nenhum contato encontrado com esse termo de busca.")
        
        return encontrados
    
    # --- REMOVER CONTATO: Remove o contato específico que foi passado
    def removerContato(self, contato):
        if contato in self.__agenda:
            self.__agenda.remove(contato)
        else:
            raise LookupError("Erro: Contato não encontrado para remoção.")

    # --- ALTERAR CONTATO EXATO: Modifica os dados do contato específico que foi passado
    def alterarContato(self, contato, novoNome=None, novoNumero=None, novoRelacao=None, novoEmail=None):
        if self.__numeroJaExiste(novoNumero):
            raise ValueError("Erro: Já existe um contato com este número.")

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