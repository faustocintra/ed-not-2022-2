"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    

def z(y, x):
    w = 0
    v = len(y) - 1
    while w <= v: 
        u = (w + v) // 2
        if x == y[u]: v = u
        elif x < y[u]: v = u - 1
        else: w = u + 1
    return -1