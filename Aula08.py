# Criando calsse com herança 
class Animal: 
    def __init__(self, nome):
        self.nome = nome 
    
    def emitir_som(self):
        print('Som do Animal')
    
class Cachorro(Animal): 
    def emitir_som(self):
        print (f'{self.nome} está latindo')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} está miando')
a1 = Cachorro('Marley')
a2 = Gato('Alfredo')

a1.emitir_som()
a2.emitir_som()
