"""
    Classe que representa uma unidade de informação
    na lista duplamente encadeada
"""
class Node:

    """ Método construtor """
    def __init__(self, data):
        self.prev = None        # Ponteiro para o nodo anterior
        self.data = data        # Dado do usuário
        self.next = None        # Ponteiro para o nodo seguinte

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o nodo anterior
    e o próximo nodo da sequência. Não tem restrição de acesso -
    inserções, exclusões e consultas podem ser realizadas em
    qualquer posição da lista.
"""
class DoublyLinkedList:

    """ Método construtor """
    def __init__(self):
        self.__head = None      # Ponteiro para o primeiro nodo
        self.__tail = None      # Ponteiro para o último nodo
        self.__count = 0        # Quantidade de nodos

    """ Método que retorna se a lista está vazia ou não """
    def is_empty(self):
        return self.__count == 0

    """
        Método privado que encontra e retorna o nodo da 
        posição especificada
    """
    def __find_node(self, pos):
        # 1º caso: posição 0, retorna __head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1)
        if pos == self.__count - 1: return self.__tail

        # 3º caso: nodo em posição intermediária

        # Se a posição estiver na primeira metade da lista,
        # faz o percurso a partir de __head, seguindo next
        elif pos < self.__count // 2:
            # Percorre a lista quantas vezes for necessário
            # para encontrar o nodo
            node = self.__head  # Começa pelo primeiro nodo
            for i in range(1, pos + 1): node = node.next
            return node

        # Senão, a posição estando na segunda metade da lista,
        # faz o percurso reverso a partir de __tail, seguindo
        # prev
        else:
            node = self.__tail  # Começa pelo último nodo
            for i in range(self.__count - 2, pos - 1, -1):
                node = node.prev
            return node


    """ Método que insere um novo valor à lista """
    def insert(self, pos, val):

        # Criamos um novo nodo para armazenar a informação
        # do usuário e também os ponteiros prev e next, ambos
        # apontando para None
        inserted = Node(val)

        # 1º caso: a lista está vazia e este é o primeiro nod
        # a ser inserido
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3º caso: inserção na posição final
        # Obs.: consideramos como posição final qualquer valor
        # que seja >= self.__count
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        elif pos > 0:
            # Encontra o nodo que atualmente ocupa a posição de inserção
            current = self.__find_node(pos)
            # Determina o nodo anterior à posição de inserção
            before = current.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = current
            current.prev = inserted

        # Incrementa a contagem de nodos
        self.__count += 1

    """ Método de atalho para inserção no início da lista """
    def insert_front(self, val):
        self.insert(0, val)

    """ Método de atalho para inserção no final da lista """
    def insert_back(self, val):
        self.insert(self.__count, val)

    """
        Método que remove o nodo da posição especificada
    """
    def remove(self, pos):

        # 1º caso: lista vazia ou posição fora dos limites da lista
        if self.__count == 0 or pos < 0 or pos > self.__count - 1:
            raise Exception("ERRO: posição inválida para remoção.")

        # 2º caso: remoção do início da lista (posição 0)
        if pos == 0:
            # Será removido o primeiro nodo da lista
            removed = self.__head
            # O novo __head passa a ser o sucessor do nodo removido
            self.__head = removed.next
            # Se o novo __head for um nodo válido, ele não pode ter
            # antecessor
            if self.__head is not None: self.__head.prev = None
            # Em caso de remoção do único nodo restante da lista,
            # __tail precisa passar a valer None também
            if self.__count == 1: self.__tail = None

        # 3º caso: remoção do final da lista (posição __count - 1)
        elif pos == self.__count - 1:
            # Será removido o último nodo da lista
            removed = self.__tail
            # O novo __tail passa a ser o antecessor do nodo removido
            self.__tail = removed.prev
            # Se o novo __tail for um nodo válido, ele não pode ter
            # sucessor
            if self.__tail is not None: self.__tail.next = None
            # Em caso de remoção do único nodo restante da lista,
            # __head precisa passar a valer None também
            if self.__count == 1: self.__head = None

        # 4º caso: remoção em posição intermediária
        else:
            # Encontra o nodo que será removido
            removed = self.__find_node(pos)
            before = removed.prev   # Nodo anterior
            after = removed.next    # Nodo posterior
            # O nodo anterior passa a apontar, à frente, para nodo posterior
            before.next = after
            # O nodo posteror passa a apontar, para trás, para o nodo anterior
            after.prev = before

        # Decrementa a quantidade de itens da lista
        self.__count -= 1
        # Retorna o dado de usuário armazenado no nodo removido
        return removed.data

    """ Método de atalho para remoção de início """
    def remove_front(self):
        return self.remove(0)

    """ Método de atalho para remoção do final """
    def remove_back(self):
        return self.remove(self.__count - 1)

    """ Método que permite consultar o conteúdo de um nodo, sem removê-lo """
    def peek(self, pos):
        # Verifica se a posição passada existe na lista
        if pos < 0 or pos >= self.__count:
            raise Exception('ERRO: impossível consultar de uma posição inexistente.')

        node = self.__find_node(pos)
        return node.data

    """ Método de atalho para consultar o primeiro nodo """
    def peek_front(self):
        return self.peek(0)

    """ Método de atalho para consultar o último nodo """
    def peek_back(self):
        return self.peek(self.__count - 1)

    """ Método que permite visualizar a estrutura como string """
    def __str__(self):
        output = ""
        node = self.__head
        for pos in range(self.__count):
            if output != "": output += ", "
            output += f"({pos}) => {node.data}"
            node = node.next
        return f"[ {output} ], count: {self.__count}"