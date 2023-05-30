
# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password


c1 = Connection()

print(c1.user) # None
print(c1.password) # None

print('\033[34m-=' * 20)

c1.set_user('Leandro')
c1.set_password('123456')

print(c1.user)
print(c1.password)