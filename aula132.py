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
        self._cor_tampa = None

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

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


######################################


caneta = Caneta('Azul')
#setter recebeu uma entrada para mudança de cor
caneta.cor = 'Pink'
#getter - > obter valor
print(caneta.cor)
print("-=" * 25)
print(caneta.cor_tampa)
caneta.cor_tampa = 'Laranja'
print(caneta.cor_tampa)


