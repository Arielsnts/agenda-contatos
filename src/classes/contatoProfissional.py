from classes.contato import Contato
import re

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoProfissional(Contato):
    def __init__(self, nome, numero, email):
        super().__init__(nome, numero)
        self.__email = self.__validarEmail(email)

    # --- OBTER EMAIL: Retorna o email profissional
    def getEmail(self):
        return self.__email
    
    # --- DEFINIR EMAIL: Altera o email profissional com validação
    def setEmail(self, email):
        self.__email = self.__validarEmail(email)

    # --- MÉTODO PRIVADO: Valida o formato do email (versão mais tolerante)
    def __validarEmail(self, email):
        if not email or not email.strip():
            raise ValueError("Erro: Email não pode estar vazio.")
        
        email = email.strip()
        
        # Validação básica: deve conter @ e pelo menos um ponto após o @
        if '@' not in email:
            raise ValueError("Erro: Email deve conter @.")
        
        partes = email.split('@')
        if len(partes) != 2:
            raise ValueError("Erro: Email deve conter apenas um @.")
        
        nome_parte, dominio = partes
        if not nome_parte or not dominio:
            raise ValueError("Erro: Email inválido.")
        
        if '.' not in dominio:
            raise ValueError("Erro: Domínio do email deve conter pelo menos um ponto.")
        
        return email

    # --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos profissionais
    # --- IMPRIMIR: Mostra todos os dados incluindo o email profissional
    def imprimir(self):
        super().imprimir()
        print("Email: ", self.__email)

    # ---json
    # --- CONVERTER PARA DICIONÁRIO: Prepara os dados para salvar em JSON
    def to_dict(self):
        return {
            "tipo": "profissional",
            "nome": self.getNome(),
            "numero": super()._desformatarNumero(self.getNumero()),
            "email": self.__email
        }

    # --- CRIAR A PARTIR DE DICIONÁRIO: Recupera contato salvo em JSON
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("nome"),
            data.get("numero"),
            data.get("email")
        )
