# Função para calcular a soma e a média de uma lista de números
def calcular_soma_e_media( rosa ):
    soma = sum( rosa )
    media = soma / len( rosa )
    return soma, media


def substituir_palavra(lista, palavra_procurada, nova_palavra):
    for i in range(len(lista)):
        if lista[i] == palavra_procurada:
            lista[i] = nova_palavra
            return lista


def gerartriangulo(n):
    for i in range(1,n + 1):
        print ("*"  * i )

print (" -----media e soma-----")
print(calcular_soma_e_media([4,  5, 6, 7]))
print ("")

print ("-----substituir palavra-----")
print(substituir_palavra(["banana","morango","limão"],'morango' , 'maça'))
print("")


print("-----gerar triangulo-----")
gerartriangulo(10)
