"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def z(y, x = 0, w = None):
    if w is None: w = len(y) - 1
    if w <= x: return
    v = w
    u = x - 1
    for t in range(x, w):
        if y[t] < y[v]:
            w += 1
            if t != u and y[t] < y[u]:
                y[t], y[u] = y[u], y[t]
    w += 1
    if v != u and y[v] < y[w]:
        y[v], y[u] = y[u], y[v]
    z(y, x, u - 1)
    z(y, u + 1, w)