from classes.contato import Contato

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoProfissional(Contato):
    def __init__(self, nome, numero, email):
        super().__init__(nome, numero)
        self.__email = email

    # --- OBTER EMAIL: Retorna o email profissional
    def getEmail(self):
        return self.__email
    
    # --- DEFINIR EMAIL: Altera o email profissional
    def setEmail(self, email):
        self.__email = email

    # --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos profissionais
    # --- IMPRIMIR: Mostra todos os dados incluindo o email profissional
    def imprimir(self):
        super().imprimir()
        print("Email: ", self.__email)

    # ---json
    def to_dict(self):
        return {
            "tipo": "profissional",
            "nome": self.getNome(),
            "numero": super()._desformatarNumero(self.getNumero()),
            "email": self.__email
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("nome"),
            data.get("numero"),
            data.get("email")
        )