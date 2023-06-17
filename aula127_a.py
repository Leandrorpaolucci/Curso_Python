import json

CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Leandro', 27)
p2 = Pessoa('Gabriel', 25)
p3 = Pessoa('Gustavo', 23)
p4 = Pessoa('Camila', 21)

bd = [vars(p1), vars(p2), p3.__dict__, vars(p4)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print("FAZENDO DUMP")
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()
