class Cozinheiro(object):

    def cozinhar_almoço(self):
        print("Cozinheiro fazendo o almoço!!")


class Ajudante(object):

    def lavar_louca_almoco(self):
        print("Ajudante lavando a louça do almoço!!")


class MaridoDoAno(Cozinheiro, Ajudante):

    def __init__(self, nome):
        self.nome = nome

joao = MaridoDoAno("Joao")

joao.cozinhar_almoço()
joao.lavar_louca_almoco()

print(f'O {joao.nome} é o marido do ano!!!')