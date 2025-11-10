class Pessoa:
    def __init__(self, nome, idade, modelo, ano):
        self.nome = nome 
        self.idade = idade 
        self.modelo = modelo 
        self.ano = ano 
    def apresentar1(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos.')

    def apresentar2(self):
        print(f'Meu carro é do modelo {self.modelo} e o ano é {self.ano}')
pessoa1 = Pessoa('Bernardo', 18, 'civic', 2020)
pessoa1.apresentar1()
pessoa1.apresentar2()

#Encapsulamento
# - Consiste em agrupar dados através de níveis de segurança 
# 'nome' = público
# - '_privado' = Só pode ser chamado direto na classe
# - '__secreto' = não pode sofre modificação 
