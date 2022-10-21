"""
    Programa que analisa a quantidade de parênteses que abrem e fecham
    em uma expressão matemática.
"""

from lib.stack import Stack

# expr = "2 + ((5 * (3 - 2 + 1) / 4))"
# expr = "2 + ((5 * (3 - 2 + 1)) / 4))"
expr = "(2 + ((5 * (3 - (2 + 1) / 4))"

print(f"Expressão analisada: {expr}")

pilha = Stack()

# Percorre a expressão em busca de parênteses
for pos in range(len(expr)):
    # Empilha a posição em que os abre parênteses
    # foram encontrados
    if expr[pos] == "(": 
        pilha.push(pos)
        # print(pilha)

    # Desempilha a posição do último abre parêntese
    # quando um fecha parêntese é encontrado
    elif expr[pos] == ")":
        if pilha.is_empty():
            print(f"ERRO: parêntese fechando na posição {pos} não possui a abertura correspondente")
        else:
            pos_abre = pilha.pop()
            print(f"Parêntese aberto na posição {pos_abre} foi fechado na posição {pos}")
            # print(pilha)

# Percorre a pilha em busca de sobras que indicam o excesso
# de parênteses abrindo
while not pilha.is_empty():
    pos_abre = pilha.pop()
    print(f"ERRO: parêntese abrindo na posição {pos_abre} não possui o fechamento correspondente")