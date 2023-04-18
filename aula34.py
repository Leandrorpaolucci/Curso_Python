"""
Repetições
while (enquanto)
execua uma ação enquanto uma condição for verdadeira
loop infinito - > quando um código não tem fim
"""
condicao = True
while condicao:
    nome = input("Digite o seu nome: ")
    print(f"Seu nome é {nome}")
    print("Digite 'sair', para encerrar")
    if nome == 'sair':
        break

print("Você clicou em sair")


