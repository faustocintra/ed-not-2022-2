"""
    Um dicionário é uma estrutura de dados fornecida pela linguagem Python,
    capaz de armazenar múltiplos valores em uma única variável, por meio
    de pares de chave-valor.
"""

# Um dicionário é delimitado por chaves {}
# As posições nomeadas de um dicionário são chamadas PROPRIEDADES
pessoa = {
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 71,
    "peso": 76,
    "altura": 1.66
}

# Acessando os valores armazenados no dicionário
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print(f"Peso: {pessoa['peso']}")
print(f'Altura: {pessoa["altura"]}')

# Calculando o IMC (Índice de Massa Corporal) da pessoa
imc = pessoa["peso"] / pessoa["altura"] ** 2
print(f"O IMC de {pessoa['nome']} é {imc}.")

#######################################################################

# Representando formas geométricas planas por meio de dicionários

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" # retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" # triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" # elipse
}

# forma4 = {
#     "base": 22,
#     "altura": 6,
#     "tipo": 5
# }

# Função que calcula a área de uma forma geométrica plana
# sabendo as medidas da base e da altura e o tipo de forma
from math import pi

def calc_area(forma):
    if forma["tipo"] == "R":    # retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":  # triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":  # elipse/círculo
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else:   # Forma desconhecida
        return None

print('-' * 80)

print(f"Forma: {forma1['tipo']}; base: {forma1['base']}; altura: {forma1['altura']}; área: {calc_area(forma1)}")

print(f"Forma: {forma2['tipo']}; base: {forma2['base']}; altura: {forma2['altura']}; área: {calc_area(forma2)}")

print(f"Forma: {forma3['tipo']}; base: {forma3['base']}; altura: {forma3['altura']}; área: {calc_area(forma3)}")

# print(f"Forma: {forma4['tipo']}; base: {forma4['base']}; altura: {forma4['altura']}; área: {calc_area(forma4)}")