
class Contato:
    def __init__(self, nome, numero, DDD, email):
        self.__nome = nome
        self.__numero = numero
        self.__DDD = DDD
        self.__email = email



    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero
    
    def getDDD(self):
        return self.__DDD
    
    def getEmail(self):
        return self.__email
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def setDDD(self, ddd):
        self.__DDD = ddd
    
    def setEmail(self, email):
        self.__email = email


    def imprime (self):
        print("Nome:", self.__nome)
        print ("Número:", self.__numero)
        print ("DDD:", self.__DDD)
        print ("Email:", self.__email)

    


