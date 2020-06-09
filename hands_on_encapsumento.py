class Conta(object):

    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return int(self._saldo)

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Falha ao atribuir saldo. Não é permitido valores negativos")
        else:
            self._saldo = saldo


class Cliente(object):

    def __init__(self, conta):
        self._conta = conta


conta_1 = Conta()
conta_1.saldo = float(input("Forneça o saldo: "))

saldo_usuario = conta_1.saldo

print(f"Saldo lido da conta {saldo_usuario}")

cliente_1 = Cliente(conta_1)

