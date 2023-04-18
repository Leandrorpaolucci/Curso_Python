"""

Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador


"""
#texto = iter('Leandro') # __iter__()

#print(texto.__next__())
#print(next(texto))


texto = 'Leandro' # iterável
iterator = iter(texto) # iterator

while True:
    letra = next(iterator)
    print(letra)
    try:
        print(next(iterator))
    except StopIteration:
        break
