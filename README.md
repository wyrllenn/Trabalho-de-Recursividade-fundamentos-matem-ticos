Relatório de Implementações Recursivas em Fundamentos Matemáticos
Discentes: Yarlley Wyrllenn e Joseane Isabela
Docente: Jayor Nessi Teixeira
Instituição: Universidade Federal de Santa Catarina (UFSC)
Disciplina
Fundamentos: Matemáticos Introdução
Este relatório detalha a implementação e o funcionamento de três algoritmos fundamentais que exemplificam o conceito de recursão em programação e suas aplicações em problemas matemáticos e de busca: Busca Binária, Cálculo de Fatorial e Torres de Hanói. A recursão, uma técnica onde uma função chama a si mesma para resolver um problema menor da mesma natureza, é um pilar crucial na ciência da computação e na matemática discreta, permitindo soluções elegantes e eficientes para problemas complexos.


1. Busca Binária

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

Descrição da Função busca_binaria
A função busca_binaria implementa um algoritmo de busca eficiente para encontrar um valor_alvo em uma lista ordenada. Sua eficiência reside na estratégia de "dividir e conquistar", eliminando metade dos elementos da lista a cada passo.
Parâmetros
lista: A lista ordenada onde a busca será realizada.
valor_alvo: O valor a ser encontrado.
inicio: Índice inicial da sub-lista para busca (padrão: 0).
fim: Índice final da sub-lista para busca (padrão: len(lista) - 1).
Funcionamento
Condição de Parada (Caso Base - Valor Não Encontrado): Se inicio > fim, a sub-lista está vazia, indicando que o valor_alvo não foi encontrado. Retorna -1.
Cálculo do Meio: Determina o índice do elemento central da sub-lista atual.
Caso Base (Valor Encontrado): Se lista[meio] for igual a valor_alvo, o valor foi encontrado e seu índice (meio) é retornado.
Chamada Recursiva - Metade Esquerda: Se valor_alvo < lista[meio], a busca continua na metade esquerda da sub-lista (inicio a meio - 1).
Chamada Recursiva - Metade Direita: Se valor_alvo > lista[meio], a busca continua na metade direita da sub-lista (meio + 1 a fim).
Vantagens e Limitações
Vantagem: Extremamente eficiente para listas grandes, com complexidade de tempo logarítmica (O(log n)).
Limitação: Requer que a lista esteja obrigatoriamente ordenada.
Bloco de Teste (if __name__ == "__main__":)
Este bloco demonstra a utilização da função:

Define uma lista_ordenada de exemplo.
Solicita ao usuário um número para procurar.
Realiza a busca e informa se o número foi encontrado e em qual índice, ou se não foi encontrado.
Inclui tratamento de erro (try...except ValueError) para entradas não numéricas.


2. Função Fatorial

def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero-1)

valor = float(input("Digite um número: "))


if valor < 0 or valor != int(valor):
    print("Número inválido para o cálculo.")
else:   
    resultado = fatorial(valor)
    print(f"O resultado do número {valor}! foi {resultado}.")
    

# Fatorial recursivo: retorna numero * fatorial(numero - 1), reduzindo o problema até o caso base. Caso base: se numero 
# <= 1 retorna 1 (garante 0! = 1 e 1! = 1). Quando é determinado o caso base é limitado a conta até o valor 1 assim 
# impedido que continue infinitamente o que geraria erro ao cálculo.
#
# Exemplo (valor = 4):
#
#    fatorial(4) = 4 * fatorial(3)
#                = 4 * 3 * fatorial(2)
#                = 4 * 3 * 2 * fatorial(1)
#                = 4 * 3 * 2 * 1 = 24

Descrição da Função fatorial
A função fatorial calcula o fatorial de um número inteiro não negativo utilizando recursão. O fatorial de um número n (denotado por n!) é o produto de todos os inteiros positivos menores ou iguais a n.
Parâmetro
numero: O número inteiro não negativo para o qual o fatorial será calculado.
Funcionamento
Condição de Parada (Caso Base): Se numero <= 1, a função retorna 1. Isso cobre 0! = 1 e 1! = 1, impedindo a recursão infinita.
Chamada Recursiva: Se numero > 1, a função retorna o produto de numero pelo resultado da chamada recursiva para fatorial(numero - 1).
Exemplo de Execução
Para fatorial(4):

fatorial(4) retorna 4 * fatorial(3)
fatorial(3) retorna 3 * fatorial(2)
fatorial(2) retorna 2 * fatorial(1)
fatorial(1) retorna 1 (caso base)
Substituindo de volta: 2 * 1 = 2, então 3 * 2 = 6, e finalmente 4 * 6 = 24.
Processamento e Validação da Entrada do Usuário
Solicita ao usuário um número.
Converte a entrada para float para permitir uma validação mais robusta.
Validação: Verifica se o valor é negativo ou não é um número inteiro (valor < 0 or valor != int(valor)). O fatorial é definido apenas para inteiros não negativos.
Se a entrada for inválida, exibe uma mensagem de erro.
Se a entrada for válida, calcula e exibe o resultado do fatorial.


3. Torres de Hanói

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

Descrição da Função hanoi
A função hanoi resolve o clássico quebra-cabeça das Torres de Hanói usando uma abordagem recursiva. O objetivo é mover n discos de um pino de origem para um pino de destino, usando um pino auxiliar, com as seguintes regras:

Apenas um disco pode ser movido por vez.
Um disco maior nunca pode ser colocado sobre um disco menor.
Parâmetros
n: O número de discos a serem movidos.
origem: O pino inicial.
destino: O pino final.
auxiliar: O pino intermediário.
Funcionamento Detalhado
Condição de Parada (Caso Base): Se n == 1 (apenas um disco), o problema é trivial: move o disco diretamente da origem para o destino. Imprime a ação e retorna.
Passo Recursivo 1: Move n-1 discos da origem para o auxiliar, usando o destino como pino temporário. (hanoi(n-1, origem, auxiliar, destino))
Movimento do Maior Disco: Após os n-1 discos superiores estarem no pino auxiliar, o maior disco (disco n) é movido da origem para o destino. Imprime esta ação.
Passo Recursivo 2: Move os n-1 discos do auxiliar para o destino, usando a origem como pino temporário. (hanoi(n-1, auxiliar, destino, origem))
Bloco de Teste (if __name__ == "__main__":)
Este bloco gerencia a interação com o usuário e a execução da função:

Solicita ao usuário o numero_discos.
Valida se o número de discos é positivo.
Chama a função hanoi com os pinos 'A' (origem), 'C' (destino) e 'B' (auxiliar).
Calcula e exibe o total_movimentos necessários, que é 2**numero_discos - 1.
Inclui tratamento de erro (try...except ValueError) para entradas não numéricas.
Exemplo para 3 Discos
O documento detalha a sequência de movimentos para n = 3, ilustrando a natureza "divide e conquista" da recursão: os dois discos superiores são movidos, o maior disco é movido, e então os dois discos superiores são movidos novamente para o destino final.
Conclusões sobre Torres de Hanói
A recursão é essencial para a solução, decompondo o problema em subproblemas idênticos.
O caso base (n == 1) é vital para a terminação da recursão.
A complexidade de movimentos (2**n - 1) demonstra o crescimento exponencial com o número de discos.


Conclusão Geral
Os algoritmos de Busca Binária, Fatorial e Torres de Hanói são exemplos clássicos que demonstram a potência e a elegância da recursão. Cada um, à sua maneira, ilustra como problemas complexos podem ser divididos em instâncias menores e idênticas, culminando em uma solução final através da combinação dos resultados desses subproblemas. A compreensão da recursão, seus casos base e seus passos recursivos, é fundamental para o desenvolvimento de algoritmos eficientes e para a resolução de uma ampla gama de desafios em Fundamentos Matemáticos e Ciência da Computação.
