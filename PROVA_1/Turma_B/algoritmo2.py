"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA: Algoritmo de ordenação Selection Sort.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    z: função selection_sort
    y: a lista a ser ordenada
    x: posição do for na lista
    w: posição do menor elemento
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def z(y):
    for x in range(len(y) - 1):
        w = x + 1
        for i in range(x + 2, len(y)):
            # ERRO: if y[i] < y[x]:
            # pos_menor é representado pela variável w
            if y[i] < y[w]:
                w = i
        if y[w] < y[x]:
            y[x], y[w] = y[w], y[x]