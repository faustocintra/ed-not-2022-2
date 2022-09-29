"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def z(y):
    for x in range(len(y) - 1):
        w = x + 1
        for i in range(x + 2, len(y)):
            if y[i] < y[x]:
                w = i
        if y[w] < y[x]:
            y[x], y[w] = y[w], y[x]