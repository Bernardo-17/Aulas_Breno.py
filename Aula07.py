#Herença 
# - Quando uma classe(filha) herda atributos e métodos de outra 
# - Facilita manutenção 
# - Evita repetição do código 
# - Reaproveitamento de código 
# - Sobrescrita de métodos 

print('-------introdução á Herança-------') 
class Pai: 
    def falar(self):
        print('Olá, filhos.')
class Filho(Pai):
    pass 
f = Filho()
f.falar()
