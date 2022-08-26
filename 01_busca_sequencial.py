nums = [ 9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27 ]

"""
    Função que realiza uma busca sequencial em uma
    lista procurando val.
    Se val for encontrado, retorna a posição de val.
    Se val não for encontrado, retorna o valor -1.
"""
def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # Percorreu toda a lista e não encontrou val; retorna -1
    return -1

#######################################################

# Testes

# Procurando o número 15
# resultado = busca_sequencial(nums, 15)
# print(f"Posição do valor 15 na lista: {resultado}")

# resultado = busca_sequencial(nums, 20)
# print(f"Posição do valor 20 na lista: {resultado}")

# resultado = busca_sequencial(nums, 33)
# print(f"Posição do valor 33 na lista: {resultado}")

# Impede que a lista importada seja colocada em cache
import sys
sys.dont_write_bytecode = True

from data.primos import primos
from time import time

hora_ini = time()
print(f"Posição do número 709: {busca_sequencial(primos, 709)}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição do número 7717: {busca_sequencial(primos, 7717)}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição do número 4: {busca_sequencial(primos, 4)}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

############################################################

from data.lista_nomes import nomes

print('-' * 80)

hora_ini = time()
print(f"Posição de ADALBERTO: {busca_sequencial(nomes, 'ADALBERTO')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de LAURA: {busca_sequencial(nomes, 'LAURA')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULMIRA: {busca_sequencial(nomes, 'ZULMIRA')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ORKUTILSON: {busca_sequencial(nomes, 'ORKUTILSON')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de AARAO: {busca_sequencial(nomes, 'AARAO')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")