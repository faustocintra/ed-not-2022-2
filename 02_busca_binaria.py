"""
    ALGORITMO DE BUSCA BINÁRIA

    Dada uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas metades
    procurando pelo valor de busca apenas na metade onde
    o valor poderia estar. Novas subdivisões são feitas
    até que se encontre o valor de busca ou que reste
    apenas uma sublista vazia, quando se conclui que o
    valor de busca não existe na lista.
"""
def busca_binaria(lista, val):

    ini = 0
    fim = len(lista) - 1

    while ini <= fim:
        # Encontra o meio da lista
        meio = (ini + fim) // 2     # // -> resultado da divisão INTEIRA

        # 1º caso: o valor na posição do meio da lista
        # corresponde ao valor buscado; ENCONTRAMOS e
        # retornamos a posição encontrada (meio)
        if val == lista[meio]:
            return meio