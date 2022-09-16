"""
    ALGORITMO DE ORDENAÇÃO QUICK SORT

    Escolhe um dos elementos da lista para ser o pivô (na nossa
    implementação, o último elemento) e, na primeira passada, divide
    a lista, a partir da posição final do pivô, em uma sublista à
    esquerda, contendo apenas valores menores que o pivô, e outra
    sublista à direita, que contém apenas valores maiores que o pivô.

    Em seguida, recursivamente, repete o processo em cada uma das
    sublistas, até que a lista toda esteja ordenada.
"""

# Variáveis de estatística
passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    
    # Quando não soubermos o valor da variável "fim",
    # vamos atribuir a ela a última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que o algoritmo trabalhe, é necessário que
    # a faixa delimitada pelas variáveis "ini" e "fim"
    # tenha, pelo menos, dois elementos.
    # Caso contrário, saímos sem fazer nada
    if fim <= ini: return

    global passadas, comps, trocas

    # Inicialização das variáveis
    pivot = fim
    div = ini - 1
    passadas += 1

    # Percorre a lista da posição "ini" até a posição "fim" - 1
    for pos in range(ini, fim):
        comps += 1
        # Compara os elementos das posições "pos" e "pivot"
        if lista[pos] < lista[pivot]:
            div += 1    # Incrementa a posição do divisor
            # Se as variáveis "div" e "pos" forem diferentes entre
            # si e o elemento de "pos" for menor que o elemento de
            # "div", promove a troca entre eles
            comps += 1
            if pos != div and lista[pos] < lista[div]:
                trocas += 1
                lista[pos], lista[div] = lista[div], lista[pos] # Troca

    # Depois que o loop acaba, o divisor é incrementado ainda uma vez
    div += 1

    # Caso os valores de "div" e "pivot" sejam diferentes entre si, 
    # faz-se a comparação entre os elementos da posição "div" e da
    # posição "pivot". Caso este seja menor que aquele, promove-se a
    # troca entre eles.
    comps += 1
    if pivot != div and lista[pivot] < lista[div]:
        trocas += 1
        lista[pivot], lista[div] = lista[div], lista[pivot] # Troca

    # O elemento na posição "div" está na posição correta agora.

    # Chamamos recursivamente a função para ordenar a sublista à
    # esquerda da posição "div".
    quick_sort(lista, ini, div - 1)

    # Fazemos o mesmo para ordenar a sublista à direita de "div".
    quick_sort(lista, div + 1, fim)

########################################################################

nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

passadas = comps = trocas = 0
print("Antes:", nums)
quick_sort(nums)
print("Depois:", nums)
print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")

#############################################################

from time import time
from data.nomes_desord import nomes
import tracemalloc

passadas = comps = trocas = 0

tracemalloc.start()     # Inicia o monitoramento da memória
hora_ini = time()
quick_sort(nomes)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

# Exibe só os 1000 primeiros, para andar mais rápido
print("Depois:", nomes[:1000]) 

print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")
