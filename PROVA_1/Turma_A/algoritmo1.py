"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA: Algoritmo de ordenação Merge Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    a: função merge_sort
    b: a lista a ser ordenada
    c: meio da lista
    d: sublista da esquerda
    e: sublista da direita
    f: posição da sublista esquerda
    g: posição da sublista direita
    h: vetor ordenado
    i: vetor de sobra
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.

"""

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = b[:c]
    e = b[c:]
    d = a(d)
    e = a(e)
    f = g = 0
    h = []
    i = []
    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            # ERRO: i.append(d[f])
            # Aqui deveria ser usada a variável h
            h.append(d[f])
            f += 1
        else:
            # ERRO: i.append(e[g])
            # Aqui deveria ser usada a variável h
            h.append(e[g])
            g += 1
    if(f < g): i = d[f:]
    else: i = e[g:]
    return h + i