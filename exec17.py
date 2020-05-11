class Automovel(object):
    pass


class Motocicleta(object):
    pass


# Pegar a resposta do usuário
resp = int(input("Informe o tipo do seu veículo:\n1- Automóvel ou 2- Motocicleta:\n"))

veiculo = None

# Verifique se é um Automóvel
if resp == 1:
    # Crie um automóvel
    veiculo = Automovel()

# Verifique se é uma Motocicleta
if resp == 2:
    # Crie uma motocicleta
    veiculo = Motocicleta()

# Informe que criou uma motocicleta

if type(veiculo == Automovel):
    print(f"Você criou um automóvel:")

if type(veiculo) == Motocicleta:
    print(f"Você criou uma motocicleta")
