# Execução com operações matemáticas básicas e avançadas com o módulo "math"

import math  # Importação do Módulo "math"

def operacoes_basicas():
    # Aqui, perguntamos os números e atribuímos valores às variáveis
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))

    print("Soma:", num_1 + num_2)
    print("Subtração: ", num_1 - num_2)
    print("Multiplicação: ", num_1 * num_2)
    print("Divisão: ", num_1 / num_2) # Aqui na divisão garantir de que o usuário
                                      # Não faça uma divisão por 0
operacoes_basicas()

## Operações Avançadas com "math"

# Raiz Quadrada
def raiz_quadrada():
    num = int(input("Digite um número: "))

    print("Raiz quadrada: ", math.sqrt(num))

raiz_quadrada()

# Potência
def potencia():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um número: "))
    
    print("Potência: ", math.pow(num_1, num_2)) # Você pode fazer com - print("Potência: ", num_1 ** num_2)

potencia()

# Arredondamentos
def arredondamentos():
    num = int(input("Digite um número: "))
    
    print("Arredondado para cima: ", math.ceil(num))
    print("Arredondado para baixo: ", math.floor(num))

arredondamentos()

# Valor Absoluto
def valor_absoluto():
    num = int(input("Digite um número: "))
    
    print("Valor Absoluto: ", abs(num))
    
valor_absoluto()

