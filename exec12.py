from exec11 import calcular_imc

total_pessoas = int(input("Forneça o total de pessoas para se calcular o IMC:\n"))

for i in range(total_pessoas):
    nome = input("Forneça o nome da pessoa:\n")
    peso = float(input("Forneça o seu peso:\n"))
    altura = float(input("Forneça a sua altura:\n"))
    resultado = calcular_imc(peso, altura)

    print(f"A pessoa {nome} tem o IMC de: {resultado}")
