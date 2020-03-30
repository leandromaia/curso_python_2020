ano_atual = 2020

ano_user = int(input("Forneça o ano do seu nascimento:\n"))

resultado = ano_atual - ano_user

if resultado == 18:
    print("Vá se alistar!!!!")

elif resultado > 18:
    print("Você já passou da idade de se alistar!!!")

else:
    print("Você deve aguardar para se alistar")