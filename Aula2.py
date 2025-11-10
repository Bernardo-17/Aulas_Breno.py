# Revisão sobre Classes e Encapsulamento 
# - Revisar os conceitos de classe e objeto 
# - Identificar atributos e métodos.
# - Compreender encapsulamento e modificadores de acesso 
# - Desenvolver uma aplicação prática 

# Sobre a Prova...
# - Prova prática 
# - Conceitos trabalhados na revisão 
# - Prova e Resultado no dia

## 1. Conceitos de Classe e Objeto  
# - Classe: modelo (molde) que define atrivuyos e métodos 
# - Objeto: Instância dessa classe

# Crie uma classe Pessoa com pelo menos dois atributos e dois métodos
class Pessoa:
    def __init__(self, nome, idade, como_o_cabelo_ficou, modo_de_cortar):
        self.nome = nome
        self.idade = idade 
        self.como_o_cabelo_ficou = como_o_cabelo_ficou
        self.modo_de_cortar = modo_de_cortar

    def apresentar1(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos')

    def apresentar2(self):
        print(f'O meu cabelo ficou {self.como_o_cabelo_ficou} e quem cortou foi {self.modo_de_cortar}.')
        
pessoa1 = Pessoa('Nuno Moreira', 18, 'horrivel', 'agressivo')
pessoa1.apresentar1()
pessoa1.apresentar2()


