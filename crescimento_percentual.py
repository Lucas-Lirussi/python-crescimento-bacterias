# Projeto 1:
# Análise do crescimento percentual diário de bactérias

# Lista com o número de bactérias por dia (em milhares)
lista = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# Lista que irá armazenar os percentuais de crescimento
amostra = []

# Laço de repetição que percorre os índices da lista
for diferenca in range(1, len(lista)):

    # Valores da iteração atual
    amostra_atual = lista[diferenca]
    amostra_anterior = lista[diferenca - 1]

    # Cálculo da variação percentual
    percentual = 100 * (amostra_atual - amostra_anterior) / amostra_anterior

    # Armazena o resultado
    amostra.append(percentual)

# Resultado final
print("Variação percentual diária (%):")
print(amostra)
