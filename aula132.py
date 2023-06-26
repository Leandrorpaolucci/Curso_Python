# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        #private protected # não use isso fora da classe
        self._cor = cor

    @property #obter o valor
    def cor(self):
        print("PROPERTY")
        return self._cor
    
    @cor.setter #configurar um eventual novo valor
    def cor(self, valor):
        print('Estou no setter', valor)
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    
    def cor_tampa(self):
        ...


######################################


caneta = Caneta('Azul')
#setter recebeu uma entrada para mudança de cor
caneta.cor = 'Pink'
#getter - > obter valor
print(caneta.cor)


