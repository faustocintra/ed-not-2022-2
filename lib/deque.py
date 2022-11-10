"""
    ESTRUTURA DE DADOS DEQUE
    Deque (Double-Ended QUEue) é uma estrutura de dados derivada
    da fila que permite inserções e remoções em qualquer uma de
    suas extremidades. Com isso, o deque pode se comportar tanto
    como uma fila comum quanto como uma fila em que são admitidos
    elementos prioritários e a possibilidade de desistência do
    último elemento.
"""
class Deque:

    """ Método construtor """
    def __init__(self):
        self.__data = []        # Lista vazia

    """ Método de inserção no início """
    def insert_front(self, val):
        self.__data.insert(0, val)

    """ Método de inserção no final """
    def insert_back(self, val):
        self.__data.append(val)

    """ Método que determina se o deque está vazio """
    def is_empty(self):
        return len(self.__data) == 0

    """ Método de remoção do início """
    def remove_front(self):
        if(self.is_empty()):
            raise Exception('ERRO: impossível remover de um deque vazio.')
        return self.__data.pop(0)

    """ Método de remoção do final """
    def remove_back(self):
        if(self.is_empty()):
            raise Exception('ERRO: impossível remover de um deque vazio.')
        return self.__data.pop()

    """ Método que consulta a primeira posição """
    def peek_front(self):
        if(self.is_empty()):
            raise Exception('ERRO: impossível consultar um deque vazio.')
        return self.__data[0]

    """ Método que consulta a última posição """
    def peek_back(self):
        if(self.is_empty()):
            raise Exception('ERRO: impossível consultar um deque vazio.')
        return self.__data[-1]

    """
        Método que retorna uma representação do deque como string
    """
    def __str__(self):
        return str(self.__data)