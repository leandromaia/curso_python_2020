class Time(object):

    def __init__(self, jogadores):
        self._lista_jogadores = jogadores

    @property
    def jogadores(self):
        nomes_maiusculos = list()
        for jogador in self._lista_jogadores:
            nomes_maiusculos.append(jogador.upper())

        return nomes_maiusculos

    @jogadores.setter
    def jogadores(self, valor):
        if type(valor) == list:
            self._lista_jogadores = valor
        else:
            print("Falha ao atribuir jogadores. Deve ser uma lista!")


nomes = ['dudu', 'marcos', 'fernando prass']
verdao = Time(nomes)

# Pega os jogadores
print(verdao.jogadores)

# Atribuo valores
verdao.jogadores = ['Gustavo', "Henrique"]

