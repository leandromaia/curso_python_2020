class Pizza(object):

    def __init__(self, sabor):\
        self.sabor = sabor


nome_sabor =  input("Qual o sabor da sua pizza: ")

user_pizza = Pizza(nome_sabor)

input(f"A pizza criada foi de sabor {user_pizza.sabor}")
