"""
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT

    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando dois elementos adjacentes sempre que o 
    segundo for MENOR que o primeiro. Efetua tantas passadas
    quanto necessárias até que, na última passada, nenhuma
    troca seja efetuada. 
"""

# Variáveis de estatística
comps = trocas = passadas = 0

def bubble_sort(lista):

    global comps, passadas, trocas
    comps = trocas = passadas = 0

    # Loop eterno (não sabemos quantas passadas serão necessárias)
    while True:

        # Começa uma nova passada
        passadas += 1
        trocou = False

        # Percurso da lista, do primeiro ao último elemento
        # com acesso a cada posição

        # O loop só pode ir até a PENÚLTIMA posição
        for pos in range(len(lista) - 1):
            comps += 1
            if lista[pos + 1] < lista[pos]:
                # Efetua a troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True

        if not trocou:  # Não houve troca na passada; ESTÁ ORDENADO!
            break   # Termina o loop eterno

###################################################################

nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

# Pior caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Antes:", nums)
bubble_sort(nums)
print("Depois:", nums)
print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")

###################################################################

# from time import time
# from data.nomes_desord import nomes

# nomes_parcial = nomes[:10000]

# hora_ini = time()
# bubble_sort(nomes_parcial)  # A ordenação ocorre aqui
# hora_fim = time()

# print("Depois:", nomes_parcial)

# print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")