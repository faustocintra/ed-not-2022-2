"""
    Programa simples que inverte uma palavra e verifica se ela é
    um PALÍNDOMO, isto é, uma palavra que pode ser lida de trás
    para frente assim como da frente para trás.
    Para isso, usaremos uma estrutura de pilha baseada em uma
    lista do Python.
"""

palavra = input('Informe a palavra: ')

pilha = []  # Lista que será usada como pilha

# 1) Pega cada letra da palavra e coloca na pilha
for letra in palavra:
    # A inserção da letra se dará sempre no final (topo) da pilha
    pilha.append(letra)
    print(pilha)

print("-" * 50)

# Variável para receber a palavra remontada e invertida
inverso = ""

# 2) Vamos retirar as letras da pilha, uma a uma, DO FIM PARA O INÍCIO.
# A operação se repete enquanto a pilha não estiver vazia.
# Cada letra retirada é acrescentada à variável inverso.
while len(pilha) > 0:
    letra = pilha.pop() # Retira o último elemento da pilha
    inverso += letra    # Acrescenta a letra ao inverso
    print(pilha)

print("-" * 50)

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {inverso}")

if palavra == inverso:
    print("*** A PALAVRA É UM PALÍNDROMO ***")
else:
    print("--- A palavra não é um palíndromo :( ---")