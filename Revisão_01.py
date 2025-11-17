class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano
    def apresentar(self):
        print(f'Meu carro é da marca {self.marca}, modelo {self.modelo} e do ano {self.ano}')
carro1 = Carro('honda', 'civic', 2011)
carro1.apresentar()
