def criar_numeros_pares(inicio, fim):
    lista_num_pares = []

    for item in range(inicio, fim):
        if item % 2 == 0:
            lista_num_pares.append(item)
    return lista_num_pares

def main():
    inicio = int(input("Forneça o início do range:\n"))
    final = int(input("Forneça o final do range:\n"))

    pares = criar_numeros_pares(inicio, final)

    print(f"Entre {inicio} e {final} há um total de {len(pares)} de números pares")

    for valor in pares:
        print(f'Valor par: {valor}')

main()