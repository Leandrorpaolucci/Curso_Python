# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #O método normal, recebe self
        # setter
        self.user = user

    def set_password(self, password): #O método normal, recebe self
        self.password = password


    @classmethod # O método de classe recebe a classe
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod #Ele é uma função dentro da classe, não recebe self, nem ao cls
    def soma(x, y):
        return x + y 

    @staticmethod
    def log(msg):
        print('LOG', msg)

    @staticmethod
    def connection_log(msg):
        print('LOG', msg)


# c1 = Connection()
# print(c1.user)
# print(c1.password)
# c1.set_user('Leandro')
# c1.set_password('123456789')
# print(c1.user)
# print(c1.password)


c1 = Connection.create_user_auth('Leandro', '123456')
print(Connection.connection_log("Conexão realizada com sucesso!"))
print(c1.user)
print(c1.password)
print(Connection.soma(2,3))