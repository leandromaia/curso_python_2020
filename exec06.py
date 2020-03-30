from datetime import date

date_now = date.today()

day = int(input("Forneça o dia do seu aniversário:\n"))
mes = int(input("Forneça o mês do seu aniversário:\n"))
ano = int(input("Forneça o ano do seu aniversário:\n"))

user_niver = date(ano, mes, day)

result = date_now - user_niver
print(f'Você tem no momento {result.days} dias de vida')