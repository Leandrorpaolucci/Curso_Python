
# __dict__ e vars para atributos de instancia

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

#p1 = Pessoa('Joao', 35)
#print(p1.__dict__)
#print(vars(p1))

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)


print(vars(p1))
print(p1.nome)
