
def hanoi(n, origem, destino, auxiliar):
    # Caso base: quando há apenas 1 disco para mover
    if n == 1:
        print(f"Mover disco {n} de {origem} para {destino}")
        return
    
    # Passo 1: Mover n-1 discos da origem para o pino auxiliar
    hanoi(n-1, origem, auxiliar, destino)
    
    # Passo 2: Mover o disco n da origem para o destino
    print(f"Mover disco {n} de {origem} para {destino}")
    
    # Passo 3: Mover os n-1 discos do pino auxiliar para o destino
    hanoi(n-1, auxiliar, destino, origem)

# Teste da função
if __name__ == "__main__":
    try:
        numero_discos = int(input("Digite o número de discos: "))
        if numero_discos <= 0:
            print("Por favor, digite um número positivo de discos.")
        else:
            print(f"\nResolvendo Torres de Hanói com {numero_discos} discos:")
            hanoi(numero_discos, 'A', 'C', 'B')
            # Calcula o número total de movimentos
            total_movimentos = 2**numero_discos - 1
            print(f"\nNúmero total de movimentos: {total_movimentos}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


# Exemplo para 3 discos (origem A (primeiro), destino C (terceiro), auxiliar B (segundo)) mova os seguintes discos:
#
# disco 1 de A para C
# disco 2 de A para B
# disco 1 de C para B
# disco 3 de A para C
# disco 1 de B para A
# disco 2 de B para C
# disco 1 de A para C
#
# Quando N = 1, o único movimento será de mover disco 1 de origem para destino e retorna. Esse caso base permite que a recursão comece a 
# ser desenvolvida.

# Cálculo de movimentos para 3 discos:

# Total de movimentos = 2**3 − 1 = 7.
