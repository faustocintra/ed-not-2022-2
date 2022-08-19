# range(): função que gera uma faixa de números.
# É muito usada em associação com listas

# range() com 1 argumento: gera uma lista que vai de
# 0 (zero) até argumento - 1
for x in range(10): # Gera números de 0 a 9
    print(x)

print('-' * 80)

# range() com 2 argumentos: gera uma lista começando
# pelo primeiro argumento (inclusive) até o segundo
# argumento (exclusive)
for y in range(5, 15): # Gera números de 5 a 14
    print(y)

print('-' * 80)

# range() com três argumentos:
# 1º: limite inferior (inclusive)
# 2º: limite superior (exclusive)
# 3º: passo (de quanto em quanto a lista vai andar; pode ser NEGATIVO)
for z in range(0, 22, 3):  # Gera lista de 0 a 21, saltando de 3 em 3
    print(z)

print('-' * 80)

# range() com passo negativo
for k in range(10, 0, -1):  # Contagem regressiva de 10 a 1
    print(k)