import math

def calcular_imc(peso, altura):
    imc = peso / math.pow(altura, 2)
    return imc

def main():
    resultado = calcular_imc(80, 1.79)
    print(f'Resultado IMC: {resultado}')

main()