# 3) Crie uma classe para implementar uma conta corrente. A classe
# deve possuir os seguintes atributos:
# a) número da conta
# b) nome do correntista
# c) saldo
# Os métodos são os seguintes:
# a) alterar_nome
# b) deposito
# c) saque
# No construtor, o saldo é opcional, com valor padrão zero e os
# demais atributos são obrigatórios.

import os

class CurrentAccount:
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name.upper()
        self.balance = 0
        os.system("clear")

    def change_name(self, name):  # alterar nome
        self.name = name.upper()

    def withdraw(self, value):  # sacar
        if (self.balance - value) >= 0:
            self.balance -= value
            self.extract()
        else:
            print('Saldo insuficiente para saque!')

    def deposit(self, value):  # depositar
        if value > 0:
            self.balance += value
            self.extract()
        else:
            print('Saldo insuficiente para deposito!')

    def extract(self):
        msg = f'NOME: {self.name} \n'
        msg += f'CONTA: {self.account_number} \n'
        msg += f'SALDO: {self.balance} \n'
        print(msg)


info = CurrentAccount('1531-1', 'Diego Felipe')
info.deposit(1000)
info.deposit(500)
info.withdraw(1300)
info.change_name('Diego Felipe da Silva Bez')
info.withdraw(13.18)
