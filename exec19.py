class Torcedor(object):

    def __init__(self, nome_torcedor, idade):
        self.nome = nome_torcedor
        self.idade = idade

    def comemorar(self):
        print("Gooooollllllllllll!!!!!!!")
        print(f'Id do objeto que gritou gol: {id(self)}')
        self.cpf = 99999999

nome = input("Forneça o nome do torcerdor: ")
palmeirense = Torcedor(nome, 37)

print(f"Id do objeto torcedor {id(palmeirense)}")


#print(f"Cpf do torcerdor: {palmeirense.cpf}")


palmeirense.comemorar()
print(f"Cpf do torcerdor: {palmeirense.cpf}")
