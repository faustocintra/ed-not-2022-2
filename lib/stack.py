"""
    ESTRUTURA DE DADOS PILHA
    É uma estrutura de dados linear em que tanto a operação
    de inserção (push) quanto a operação de remoção (pop)
    acontecem no final (ou topo). Como consequência, o
    funcionamento da pilha obedece ao princípio LIFO (Last
    In, First Out): o último a entrar deve ser o primeiro
    a sair.
"""

class Stack:

    """ Método construtor """
    def __init__(self):
        # Cria uma lista privada e vazia para armazenar os
        # dados da pilha
        self.__data = []

    """
        Método para inserção
        Em pilhas, tem nome padronizado: push()
    """
    def push(self, val):
        self.__data.append(val)

    """
        Método que verifica se a pilha está ou não vazia
    """
    def is_empty(self):
        # A lista estará vazia se len(self.__data) for igual a 0,
        # retornando True
        # Não estará vazia, retornando False, nos demais casos
        return len(self.__data) == 0

    """
        Método para remoção
        Em pilhas, tem nome padronizado: pop()
    """
    def pop(self):
        if self.is_empty():     # A pilha está vazia
            raise Exception('ERRO: impossível remover de uma pilha vazia.')

        # Se chegou até aqui, a pilha NÃO está vazia, e a
        # remoção pode ocorrer
        return self.__data.pop()

    """
        Método que permite consultar o valor que está no topo da pilha,
        mas sem retirá-lo
        Em pilhas, tem nome padronizado: peek()
        ("Peek" significa "dar uma espiadinha", em inglês)
    """
    def peek(self):
        if self.is_empty():     # A pilha está vazia
            raise Exception('ERRO: impossível consultar uma pilha vazia.')

        return self.__data[-1]

    """
        Método que permite imprimir a pilha como string
    """
    def __str__(self):
        return str(self.__data)

###########################################################

# # Cria uma nova pilha
# pilha = Stack()

# # print(pilha.__data)

# # Insere valores na pilha
# pilha.push(35)
# pilha.push(29)
# pilha.push(16)

# print(pilha)

# retirado = pilha.pop()
# print(f"Retirado: {retirado}")
# print(pilha)

# consultado = pilha.peek()
# print(f"Consultado: {consultado}")
# print(pilha)