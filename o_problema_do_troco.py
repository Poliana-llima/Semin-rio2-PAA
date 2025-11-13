
def otimizar_carga_dp(peso_alvo, pesos_caixas):
    """
    Calcula o número mínimo de caixas necessário para atingir um peso-alvo
    usando Programação Dinâmica (abordagem bottom-up) e armazena o caminho.

    Args:
        peso_alvo (int): O peso total que o caminhão deve carregar (N).
        pesos_caixas (list): Lista de pesos das caixas disponíveis (m_i).

    Returns:
        tuple: (min_unidades, primeira_caixa). Retorna (None, None) se impossível.
    """

  
    INF = peso_alvo + 1
    
    min_unidades = [INF] * (peso_alvo + 1)
    
    primeira_caixa = [0] * (peso_alvo + 1)

    
    min_unidades[0] = 0

   
    for peso_atual in range(1, peso_alvo + 1):
        
        
        for peso_caixa in pesos_caixas:
            
            if peso_caixa <= peso_atual:
                
                peso_anterior = peso_atual - peso_caixa
                
                
                if min_unidades[peso_anterior] != INF:
                    
                    novo_minimo = 1 + min_unidades[peso_anterior]
                    
                    
                    if novo_minimo < min_unidades[peso_atual]:
                        min_unidades[peso_atual] = novo_minimo
                        
                        
                        primeira_caixa[peso_atual] = peso_caixa

   
    if min_unidades[peso_alvo] == INF:
        return None, None
    else:
        return min_unidades, primeira_caixa

def reconstruir_solucao(peso_alvo, primeira_caixa):
    
    combinacao = {}
    peso_restante = peso_alvo
    
    while peso_restante > 0:
        caixa_usada = primeira_caixa[peso_restante]
        
       
        combinacao[caixa_usada] = combinacao.get(caixa_usada, 0) + 1
        
        
        peso_restante -= caixa_usada
        
    return combinacao


PESO_ALVO = 50
PESOS_CAIXAS_DISPONIVEIS = [10, 5, 1] 


print(f"--- Estudo de Caso de Otimização de Carga Crítica (Demonstração DP) ---")
print(f"Peso-alvo obrigatório: {PESO_ALVO} kg")
print(f"Pesos das Caixas (Unidades): {PESOS_CAIXAS_DISPONIVEIS} kg")

min_unidades_tabela, caminho_tabela = otimizar_carga_dp(PESO_ALVO, PESOS_CAIXAS_DISPONIVEIS)

if min_unidades_tabela is not None:
    min_caixas = min_unidades_tabela[PESO_ALVO]
    
   
    combinacao = reconstruir_solucao(PESO_ALVO, caminho_tabela)
    
    
    detalhe_caixas = ", ".join(
        [f"{quantidade}x {peso}kg" for peso, quantidade in sorted(combinacao.items(), reverse=True)]
    )
    
    print(f"\nResultado Ótimo (Programação Dinâmica):")
    print(f"Número mínimo de caixas (Unidades de Manuseio): {min_caixas}")
    print(f"Detalhe da Carga Otimizada: {detalhe_caixas}")
else:
    print("\nERRO: O peso-alvo não pode ser alcançado com as caixas disponíveis.")

