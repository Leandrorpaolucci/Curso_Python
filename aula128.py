# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.


class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)  
    
    @classmethod
    def criar_pessoa_anonima(cls, nome):
        return cls(nome, 50)  

p1 = Pessoa('Leandro', 27)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

print("-=" * 30)

p2 = Pessoa.criar_com_50_anos('Gustavo')
print(p2.nome, p2.idade)

print("-=" * 30)

p3 = Pessoa.criar_pessoa_anonima()
print(p3.nome)
