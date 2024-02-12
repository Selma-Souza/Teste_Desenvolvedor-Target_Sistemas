def calcular_percentual_faturamento_por_estado(faturamento_por_estado):
    total = sum(faturamento_por_estado.values())
    percentuais = {estado: (faturamento / total) * 100 for estado, faturamento in faturamento_por_estado.items()}
    return percentuais

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais = calcular_percentual_faturamento_por_estado(faturamento_por_estado)

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')