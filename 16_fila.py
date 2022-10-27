from lib.queue import Queue

fila = Queue()

fila.enqueue('Adamastor')
fila.enqueue('Leonilda')
fila.enqueue('Orozimbo')
fila.enqueue('Valdisney')

print(fila)

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

fila.enqueue('Marcineide')
print(fila)

proximo = fila.peek()
print(f"Próximo a ser atendido: {proximo}")
print(fila)