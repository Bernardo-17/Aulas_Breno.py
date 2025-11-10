# -> Exercício
# - Criar objeto "Conta Bancaria "
# - 2 métodos 
# - Condicional dentro do método
class Conta_Bancaria: 
    def __init__(self, titular, saldo):
       self.titular = titular
       self.saldo =  saldo

    def depositar(self, valor):
        if valor > 0: 
            self.__saldo += valor 
            print(f'O nome do titular é: {self.titular}\nO saldo atual é: R${self.saldo}')
        else: 
            print(f'')
    conta = depositar('Maria', 300)
    conta.depositar(200)
