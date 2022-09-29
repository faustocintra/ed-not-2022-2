"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA: algoritmo de busca binária
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    z: função busca_binaria
    y: lista onde a busca será feita
    x: valor a ser buscado
    w: posição inicial
    v: posição final
    u: meio da lista
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    

def z(y, x):
    w = 0
    v = len(y) - 1
    while w <= v: 
        u = (w + v) // 2
        # ERRO: if x == y[u]: v = u
        # if deve retornar a posição do meio da lista
        if x == y[u]: return u
        elif x < y[u]: v = u - 1
        else: w = u + 1
    return -1