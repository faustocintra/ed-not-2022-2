"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA: Algoritmo de ordenação Bubble Sort.
    a: função bubble_sort
    b: lista a ser ordenada
    c: indicador de trocas (booleano)
    d: posição do for na lista
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                # ERRO: b[d + 1], b[c] = b[c], b[d + 1]
                # b[c] deve ser b[d]
                b[d + 1], b[d] = b[d], b[d + 1]
                c = True
        if not c:
            break