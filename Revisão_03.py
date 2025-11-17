class funcionario:
    def __init__(self, nome, funçao):
        self.nome = nome
        self.funçao = funçao

    def apresentar(self):
        print(f'O funcionário: {self.nome} \nFunção: {self.funçao}')

class Bombeiro(funcionario):
    pass
funcionario = Bombeiro('Bernardo','Combate à incêndio')
funcionario.apresentar()
