"""
    Classe é uma estrutura que representa conjuntamente dados e algoritmos.
    Uma classe pode ser comparada a uma "assadeira" com a qual se pode fazer
    diferentes "assados" (objetos), variando os "ingredientes" (dados) e o
    "modo de fazer" (algoritmos). Apesar dessa variação, todos os objetos
    criados a partir da mesma classe terão sempre o formato determinado por
    esta.
"""

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
        # Validando o valor da base
        if type(base) not in [int, float] or base <= 0:
            raise Exception(f"ERRO: a base ({base}) deve ser numérica e maior que zero.")

        # Validando o valor da altura
        if type(altura) not in [int, float] or altura <= 0:
            raise Exception(f"ERRO: a altura ({altura}) deve ser numérica e maior que zero.")

        # Validando o tipo
        if tipo not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ({tipo}) deve igual a R, T ou E.")

        # Armazenando os dados recebidos DENTRO do objeto
        self.base = base
        self.altura = altura
        self.tipo = tipo
        self.template = f"base={self.base}, altura={self.altura}, tipo={self.tipo}"

################################################################

# Criando três objetos a partir da classe
forma1 = FormaGeometrica(20, 15, 'R')
forma2 = FormaGeometrica(1.5, 3.5, 'T')
forma3 = FormaGeometrica(4, 4.2, 'E')
# forma4 = FormaGeometrica(-3, "tomate", "X")

forma1.altura = -7

print(f"forma1: {forma1.template}")
print(f"forma2: {forma2.template}")
print(f"forma3: {forma3.template}")
# print(f"forma4: {forma4.template}")

print('Altura atualizada de forma1: ', forma1.altura)