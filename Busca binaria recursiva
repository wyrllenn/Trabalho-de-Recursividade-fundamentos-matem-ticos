def busca_binaria(lista, valor_alvo, inicio=0, fim=None):
    """
    Busca binária recursiva em lista ordenada.
    Retorna o índice de 'valor_alvo' em 'lista' ou -1 se não encontrado.
    """
    # Se 'fim' não for definido, assume o último índice da lista
    if fim is None:
        fim = len(lista) - 1

    # Condição de parada: O valor não foi encontrado
    if inicio > fim:
        return -1

    # Cálculo seguro do meio (evita overflow em linguagens de baixo nível)
    meio = inicio + (fim - inicio) // 2 
    
    # Caso base 1: Valor encontrado
    if lista[meio] == valor_alvo:
        return meio
    # Caso recursivo 1: Valor está na metade esquerda
    elif valor_alvo < lista[meio]:
        return busca_binaria(lista, valor_alvo, inicio, meio - 1)
    # Caso recursivo 2: Valor está na metade direita
    else:
        return busca_binaria(lista, valor_alvo, meio + 1, fim)


if __name__ == "__main__":
    
    # 1. Definir a lista (deve estar ordenada!)
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(f"Lista para busca: {lista_ordenada}")
    
    # 2. Pedir o valor alvo ao usuário
    try:
        # Pede a entrada e tenta converter para inteiro
        entrada_valor = input("Digite o número que você quer procurar na lista: ")
        valor_procurado = int(entrada_valor)
        
    except ValueError:
        print("Erro: A entrada deve ser um número inteiro.")
        exit() # Encerra o programa se o input não for um número
        
    
    # 3. Executar a busca
    indice_encontrado = busca_binaria(lista_ordenada, valor_procurado)
    
    # 4. Mostrar o resultado
    if indice_encontrado != -1:
        print(f"\nResultado:")
        print(f"O número {valor_procurado} foi encontrado no índice {indice_encontrado}.")
    else:
        print(f"\nResultado:")
        print(f"O número {valor_procurado} não foi encontrado na lista.")
