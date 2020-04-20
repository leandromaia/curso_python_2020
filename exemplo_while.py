
def executar_exemplo_while():
    resp = 0

    while resp <= 0 or resp >= 3:
        resp = int(input("1 homem - 2 Mulher:\n"))

    print(f"Você selecionou um opção válida: {resp}")


executar_exemplo_while()
