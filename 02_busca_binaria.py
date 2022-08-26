"""
    ALGORITMO DE BUSCA BINÁRIA

    Dada uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas metades
    procurando pelo valor de busca apenas na metade onde
    o valor poderia estar. Novas subdivisões são feitas
    até que se encontre o valor de busca ou que reste
    apenas uma sublista vazia, quando se conclui que o
    valor de busca não existe na lista.
"""

comps = 0   # Variável global

def busca_binaria(lista, val):

    # Redefine a contagem de comparações
    global comps
    comps = 0

    ini = 0
    fim = len(lista) - 1

    while ini <= fim:
        # Encontra o meio da lista
        meio = (ini + fim) // 2     # // -> resultado da divisão INTEIRA

        # 1º caso: o valor na posição do meio da lista
        # corresponde ao valor buscado; ENCONTRAMOS e
        # retornamos a posição encontrada (meio)
        if val == lista[meio]:
            comps += 1
            return meio

        # 2º caso: o valor de busca é MENOR que o valor no meio da lista
        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        # 3º caso: o valor de busca é MAIOR que o valor no meio da lista
        else:
            comps += 2
            ini = meio + 1

    return -1  # Valor de busca não existe na lista

#########################################################################

# Impede que a lista importada seja colocada em cache
import sys
sys.dont_write_bytecode = True

from time import time

from data.lista_nomes import nomes

print('-' * 80)

hora_ini = time()
print(f"Posição de ADALBERTO: {busca_binaria(nomes, 'ADALBERTO')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")

hora_ini = time()
print(f"Posição de LAURA: {busca_binaria(nomes, 'LAURA')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")

hora_ini = time()
print(f"Posição de ZULMIRA: {busca_binaria(nomes, 'ZULMIRA')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")

hora_ini = time()
print(f"Posição de ORKUTILSON: {busca_binaria(nomes, 'ORKUTILSON')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")

hora_ini = time()
print(f"Posição de AARAO: {busca_binaria(nomes, 'AARAO')}")
hora_fim = time()
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")