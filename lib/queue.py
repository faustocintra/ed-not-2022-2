"""
    ESTRUTURA DE DADOS FILA
    É uma estrutura de dados linear em que a operação de inserção
    (enqueue) acontece no final (ou cauda) da estrutura, enquanto
    a operação de remoção (dequeue) ocorre no início (ou cabeça).
    Como consequência, o funcionamento da fila pode ser descrito
    como FIFO (First In, First Out): o primeiro a entrar é o
    primeiro a sair.
"""
class Queue:

    """ Método construtor """
    def __init__(self):
        self.__data = []    # Lista vazia

    """
        Método de inserção
        Em filas, tem nome padronizado: enqueue()
    """
    def enqueue(self, val):
        self.__data.append(val)