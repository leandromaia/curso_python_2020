from exec21_models import Time


lista_jogadores = list()

total_jogadores = int(input("Forneça o total de jogadores de seu time:\n"))

for x in range(total_jogadores):
    nome_jogador = input("Forneça o nome do jogador:\n")
    lista_jogadores.append(nome_jogador)

palmeiras = Time(lista_jogadores)

for jogador in palmeiras._lista_jogadores:
    print(f"Jogador escolhido: {jogador}")
