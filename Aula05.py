# classe carro com dois atributos e dois metodos 
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 
        
    def apresentar (self):
        print (f'O meu carro é um {self.marca}.')

    def apresentar1 (self):
        print(f'O meu carro é do modelo {self.modelo} \nAno {self.ano}')
carro1 = Carro('Honda', 'Civic', 2011)
carro1.apresentar()
carro1.apresentar1()



    
