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

# Consultas de itens da lista
primeiro = lista.peek_front()
ultimo = lista.peek_back()
item_pos6 = lista.peek(6)
print(f"Primeiro: {primeiro}, último: {ultimo}, pos. 6: {item_pos6}")

# Remoção do primeiro item
primeiro = lista.remove_front()
print(f"REMOVIDO, INICIAL: {primeiro}")
print(lista)

# Remoção do último item
ultimo = lista.remove_back()
print(f"REMOVIDO, FINAL: {ultimo} ")
print(lista)

# Remoção em posição intermediária (3)
item_pos3 = lista.remove(3)
print(f"REMOVIDO, POS. 3: {item_pos3}")
print(lista)

# Remoção em posição intermediária (1)
item_pos1 = lista.remove(1)
print(f"REMOVIDO, POS. 1: {item_pos1}")
print(lista)
