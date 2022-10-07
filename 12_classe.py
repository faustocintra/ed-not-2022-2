"""
    Classe é uma estrutura que representa conjuntamente dados e algoritmos.
    Uma classe pode ser comparada a uma "assadeira" com a qual se pode fazer
    diferentes "assados" (objetos), variando os "ingredientes" (dados) e o
    "modo de fazer" (algoritmos). Apesar dessa variação, todos os objetos
    criados a partir da mesma classe terão sempre o formato determinado por
    esta.
"""
from math import pi

class FormaGeometrica:

    # Uma classe pode ter, dentro de si, tanto dados quanto funções (estas
    # representando os algoritmos). Uma função especial, chamada __init__,
    # é chamada sempre que um novo objeto é criado a partir de uma classe.
    # Essa função especial é chamada de CONSTRUTOR.

    # Quando aparecem dentro de uma classe:
    # ~> funções passam a ser chamadas de MÉTODOS, e seu primeiro parâmetro
    #    é sempre chamado self, representando o próprio objeto
    # ~> variáveis passam a ser chamadas de ATRIBUTOS

    def __init__(self, base, altura, tipo):
        # Armazenando os dados recebidos DENTRO do objeto
        self.__base = base
        #self.__altura = altura
        self.set_altura(altura)
        self.__tipo = tipo

    # Método setter para o atributo __base
    def set_base(self, val):
        # Validando o valor da base
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a base ({val}) deve ser numérica e maior que zero.")
        self.__base = val

    # Método setter para o atributo __altura
    def set_altura(self, val):
        # Validando o valor da altura
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a altura ({val}) deve ser numérica e maior que zero.")
        self.__altura = val

    # Método setter para o atributo __tipo
    def set_tipo(self, val):
        # Validando o tipo
        if val not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ({val}) deve igual a R, T ou E.")
        self.__tipo = val

    # Método getter para o atributo __base
    def get_base(self):
        return self.__base
    
    # Método getter para o atributo __altura
    def get_altura(self):
        return self.__altura

    # Método getter para o atributo __tipo
    def get_tipo(self):
        return self.__tipo

    # Método que calcula a área da forma geométrica
    def calc_area(self):
        if(self.__tipo == "R"):
            return self.__base * self.__altura
        if(self.__tipo == "T"):
            return self.__base * self.__altura / 2
        if(self.__tipo == "E"):
            return (self.__base / 2) * (self.__altura / 2) * pi

    # Método que gera uma representação de um objeto como string
    def __str__(self):
        return f"base={self.__base}, altura={self.__altura}, tipo={self.__tipo}"

################################################################

# Criando três objetos a partir da classe
forma1 = FormaGeometrica(20, 15, 'R')
forma2 = FormaGeometrica(1.5, 3.5, 'T')
forma3 = FormaGeometrica(4, 4.2, 'E')
# forma4 = FormaGeometrica(-3, "tomate", "X")

print(f"forma1: {forma1}")
print(f"forma2: {forma2}")
print(f"forma3: {forma3}")
# print(f"forma4: {forma4.template}")

forma1.set_altura(9)

print('Altura atualizada de forma1: ', forma1.get_altura())

print(f'forma1: {forma1}, área => {forma1.calc_area()}')
print(f'forma1: {forma2}, área => {forma2.calc_area()}')
print(f'forma1: {forma3}, área => {forma3.calc_area()}')