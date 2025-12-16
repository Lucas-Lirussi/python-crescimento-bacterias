# Projeto 2:
# Comparação do crescimento entre duas colônias bacterianas

# Tamanho inicial das colônias A e B
colonia_a = float(4.0)
colonia_b = float(10.0)

# Taxa de crescimento diário das colônias
taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015

# Variável para contar os dias
dias = 0

# Loop que continua enquanto a colônia A for menor que a colônia B
while colonia_a < colonia_b:
    colonia_a += colonia_a * taxa_crescimento_a
    colonia_b += colonia_b * taxa_crescimento_b
    dias += 1

# Resultado final
print(f"Serão necessários {dias} dias para que a colônia A ultrapasse ou iguale a colônia B.")
