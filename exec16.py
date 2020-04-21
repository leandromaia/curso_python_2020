def pegar_alturas(total):
    lista_alturas = list()

    for i in range(total):
        lista_alturas.append(int(input(f"Forneça a altura {i + 1}:\n ")))
    return lista_alturas

def pegar_idades(total):
    lista_idades = []

    for x in range(total):
        lista_idades.append(int(input(f'Forneça a idade {x + 1}:\n')))
    return lista_idades

def iniciar():
    total_pessoas = int(input("Forneça o total de pessoas:\n"))
    alturas = pegar_alturas(total_pessoas)
    idades = pegar_idades(total_pessoas)

    alturas.reverse()
    idades.reverse()

    print("Confira os valores das listas invertidas")
    for i, altura in enumerate(alturas, 1):
        print(f'Altura {i}: {altura}')

    for i, idade in enumerate(idades, 1):
        print(f'Idade {i}: {idade}')

iniciar()
