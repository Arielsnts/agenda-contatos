# --- CLASSE BASE: utiliza o conceito de herança sendo a base para mais duas classes que reaproveitam seus atributos e métodos

class Contato:
    def __init__(self, nome, numero):
        self.__nome = self.__validarNome(nome)
        self.__numero = self.__formatarNumero(numero)

    # --- OBTER NOME: Retorna o nome do contato
    def getNome(self):
        return self.__nome
    
    # --- OBTER NÚMERO: Retorna o número formatado
    def getNumero(self):
        return self.__numero
    
    # --- DEFINIR NOME: Altera o nome do contato com validação
    def setNome(self, nome):
        self.__nome = self.__validarNome(nome)
    
    # --- DEFINIR NÚMERO: Altera e formata o número
    def setNumero(self, numero):
        self.__numero = self.__formatarNumero(numero)

    # --- MÉTODO PRIVADO: Valida o nome do contato (versão mais tolerante)
    def __validarNome(self, nome):
        if not nome or not nome.strip():
            raise ValueError("Erro: Nome não pode estar vazio.")
        
        nome = nome.strip()
        
        # Verifica comprimento mínimo
        if len(nome) < 2:
            raise ValueError("Erro: Nome deve ter pelo menos 2 caracteres.")
        
        # Capitaliza cada palavra (mantém acentos)
        return ' '.join(word.capitalize() for word in nome.split())

    # --- MÉTODO PRIVADO: aplica o conceito de encapsulamento elaborado no design de classes
    # --- FORMATAR NÚMERO: Valida e formata o número para o padrão (XX) 9 XXXX-XXXX (versão mais tolerante)
    def __formatarNumero(self, numero):
        # Remove espaços, parênteses e traços para validação
        numero_limpo = ''.join(filter(str.isdigit, str(numero)))
        
        if len(numero_limpo) != 11:
            raise ValueError("Erro: O número deve conter exatamente 11 dígitos.")
        
        if numero_limpo[2] != "9":
            raise ValueError("Erro: O número deve começar com 9 após o DDD.")
        
        # Validação básica de DDD (apenas verifica se está na faixa válida)
        ddd = int(numero_limpo[0:2])
        if ddd < 11 or ddd > 99:
            raise ValueError(f"Erro: DDD {ddd} não é válido.")
        
        return f"({numero_limpo[0:2]}) {numero_limpo[2]} {numero_limpo[3:7]}-{numero_limpo[7:]}"
    
    # --- IMPRIMIR: Mostra os dados básicos do contato
    def imprimir(self):
        print("Nome:", self.__nome)
        print("Número:", self.__numero)