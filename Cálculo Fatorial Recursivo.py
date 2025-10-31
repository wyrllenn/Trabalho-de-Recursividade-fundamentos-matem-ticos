
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