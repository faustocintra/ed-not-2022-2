# Lista
frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibir apenas seus elementos,
# usamos for..in, como já vimos
for f in frutas:
    print(f)

print('-' * 80)

# Se quisermos percorrer a lista em ordem inversa para exibir
# apenas os elementos, usamos for..in combinado com reversed()
for a in reversed(frutas):
    print(a)

print('-' * 80)

# Agora, se precisarmos exibir, além da informação sobre o elemento,
# também a sua POSIÇÃO, devemos usar range()
for pos in range(len(frutas)):
    print(f"{pos}: {frutas[pos]}")

print('-' * 80)

# Percurso reverso usando range() com 3 argumentos
for pos in range(len(frutas) - 1, -1, -1):
    print(f"{pos}: {frutas[pos]}")