while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro numero: ")
    operador = input("Digite o perador  Soma + | Subtração - | Divisão  / | Multiplicação *: ")

    numeros_validos = None
    num_1_float = 0
    numero_2_float = 0

    try:
        num_1_float = float(numero_1)
        numero_2_float = float(numero_2)

        numeros_validos = True
    
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros digitados são inválidos.")
        continue


    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue
    print("Realizando a sua conta: ")
    if operador == '+':
        print(f"A soma de {num_1_float} + {numero_2_float} é: {num_1_float + numero_2_float} ")
    elif operador == '-':
        print(f"A subtracao de {num_1_float} - {numero_2_float} é: {num_1_float - numero_2_float} ")
    elif operador == '/':
        print(f"A Divisão de {num_1_float} / {numero_2_float} é: {num_1_float / numero_2_float} ")
    elif operador == '*':
        print(f"A multiplicacao de {num_1_float} * {numero_2_float} é: {num_1_float * num_1_float} ")
    else:
        print("Nunca deveria chegar aqui.")
    
    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break
    