class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo 
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print(f'O carro {self.marca} está ligado')

        else: 
            self.ligado = False 
            print(f'O carro {self.marca} está desligado')
            
    def apresentar(self):
        print(f'O meu carro é da marca {self.marca} e modelo {self.modelo}')

meu_carro = Carro('Porshe', 911 )
meu_carro.ligar()
meu_carro.apresentar()
