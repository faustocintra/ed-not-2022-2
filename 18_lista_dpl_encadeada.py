from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()

print(lista)

# Inserções feitas no final da lista
lista.insert_back('1 kg tomate')
lista.insert_back('1 pct macarrão')
lista.insert_back('300g muçarela')
print(lista)

# Inserções feitas no início da lista
lista.insert_front('1 L óleo de soja')
lista.insert_front('500g sal')
lista.insert_front('2 L leite semidesnatado')
print(lista)

# Inserção intermediária na posição 3
lista.insert(3, '2 kg batata')
print(lista)

# Inserção intermediária na posição 5
lista.insert(5, '1 cx caldo de galinha')
print(lista)

# Inserção em posição não existente, >= count
lista.insert(15, '5 kg arroz')
print(lista)
