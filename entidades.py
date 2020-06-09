class Pessoa(object):

    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo


class Cidadao(Pessoa):

    def __init__(self, nome, idade, sexo, cpf):
        super().__init__(nome, sexo, idade)
        self._cpf = cpf

class Atleta(Pessoa):
    pass

class Aluno(Pessoa):
    pass

class Morador(Aluno, Cidadao, Atleta):
    pass

morador_A = Morador('jose', 23, m, 000000)
