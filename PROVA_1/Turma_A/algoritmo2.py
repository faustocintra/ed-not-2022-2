"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA: Algoritmo de busca binária
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    a: função busca_binaria
    b: lista onde a busca é feita
    c: o valor a ser buscado
    d: posição inicial
    e: posição final
    f: meio da lista
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    

def a(b, c):
    d = 0
    e = len(b) - 1
    while d <= e: 
        f = (d + e) // 2
        # ERRO: if c == b[f]: e = f
        # Aqui deve ser retornado o valor do meio
        if c == b[f]: return f
        elif c < b[f]: e = f - 1
        else: d = f + 1
    return -1