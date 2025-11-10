#1) O que é uma classe?
#- **Classe** é um modelo que define atributos (características) e métodos (ações) a um objeto.
#- **Objeto** é uma instância da classe.
#2) Primeira Classe: 'Pessoa'
#- 'def'__init__: inicializa os atributos do objeto.
#'self' representa o próprio objeto.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f'Olá, sou {self.nome} e tenho {self.idade} anos.')
pessoa1 = Pessoa("Nuno Moreira", 17)
pessoa1.apresentar()
