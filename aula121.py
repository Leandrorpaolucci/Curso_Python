# Métodos em instâncias de classe em Python
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
#print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

print('-=-=' * 25)

celta = Carro('Celta')
#print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)
