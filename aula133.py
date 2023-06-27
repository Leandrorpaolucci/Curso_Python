# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privated'

        self._metodo_protected()

    def metodo_publico(self):
        #self._metodo_protected()
        #print(self._protected)
        print(self.__private)
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_privated(self):
        print('metodo privated')
        return '__metodo_privated'

f = Foo()
# print(f._protected)
# print(f._metodo_protected())
#print(f.public)
print(f.metodo_publico())
#print(f.__metodo_privated())
#print(f._Foo__metodo_privated())