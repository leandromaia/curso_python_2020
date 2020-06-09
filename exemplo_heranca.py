class Pai(object):
    olhos = 'azul'
    nome = 'Gilberto'

    # def falar_ingles(self):
    #     print('The cat is on the table!!!')


class Mae(object):
    olhos = 'preto'
    nome = "Maria"
    altura = 1.7

    def falar_ingles(self):
        print("The book is on the table!!")


class Filha(Pai, Mae):
    residencia = "Ilha Bela"
    nome = 'Isabela'

    def __init__(self, passed_olhos):
        self.olhos = passed_olhos

    def falar_ingles(self):
        super().falar_ingles()
        print('The dog in on the table!!')

