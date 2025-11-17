class Conta_Bancaria:
    def __init__(self, titular, __saldo):
        self.titular = titular
        self.__saldo = __saldo

    def depositar(self, valor):

        if valor > 0:
            self.__saldo += valor
            print (f'O nome do titular: {self.titular} \nO saldo atual da conta: R${self.__saldo} \nDeposito feito de R${valor}')
        else:
            print(f'Não há nenhum deposito na conta de Titular: {self.titular} \nSaldo atual: R${self.__saldo}')

    def sacar(self, valor): 
        if valor > self.__saldo:
            print ('Valor de tenativa de saque acima do saldo da conta')
        elif valor > 0:
            self.__saldo -= valor
            print(f'O nome do titular da conta: {self.titular} \nSaldo atual da conta: R${self.__saldo} \nSaque feito de R${valor}')
        else:
            print(f'Não há nenhum saque feito na conta de titular: {self.titular} \nSaldo atual: R${self.__saldo}')

Conta1 = Conta_Bancaria('Bernardo', 200)
Conta1.depositar(100)
Conta1.sacar
