def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, end=" - ")
    print("Idade:", idade, end=" - ")
    print("Cidade:", cidade + "!")
    
# Exemplo de uso da função
imprimir_informacoes("Alice", 25, "São Paulo")


def calcular_operacao(num1, num2, operacao):
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero!"
    else:
        resultado = "Erro: Operação inválida!"
    
    print("Resultado da operação", num1, operacao, num2, "é:", resultado)
    
# Números fornecidos
numero1 = 1
numero2 = 2
# Operação desejada
operacao_desejada = '+'

# Calculando e imprimindo o resultado da operação especificada
calcular_operacao(numero1, numero2, operacao_desejada)


def lista_de_compras():
    # Exemplo de entrada fornecido
    entrada = "leite, ovos, pão, manteiga"

    # Separando os itens da entrada usando a vírgula como delimitador e armazenando-os em uma lista
    itens = entrada.split(',')

    # Iterando sobre os itens da lista e imprimindo cada um deles em uma linha separada
    for i, item in enumerate(itens, start=1):
        print("Item", i, ":", item.strip())

# Chamando a função lista_de_compras
lista_de_compras()



def converter_para_fahrenheit():
    # Solicitando a temperatura em Celsius ao usuário
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Convertendo Celsius para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprimindo o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit, "°F")

# Chamando a função para realizar a conversão
converter_para_fahrenheit()



 
def solicitar_nomes():
    # Lista para armazenar os nomes digitados
    nomes = []

    # Loop para continuar pedindo ao usuário para digitar nomes até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        if nome.lower() == 'sair':
            break
        else:
            nomes.append(nome)

    # Incluindo o nome "Diogo" nos nomes digitados
    nomes.append("Diogo")

    # Imprimindo todos os nomes digitados, um em cada linha
    for nome in nomes:
        print(nome)

# Chamando a função para solicitar nomes e imprimir
solicitar_nomes()
