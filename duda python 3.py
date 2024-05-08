# Cria um novo arquivo, escreve e fecha
with open('outro_arquivo.txt', 'w') as arquivo:
    arquivo.write('Este é um novo arquivo\ncom uma nova linha')

# Abre o arquivo para leitura e escrita
with open('outro_arquivo.txt', 'r+') as arquivo:
    conteudo = arquivo.read()  # Conteúdo lido do arquivo
    arquivo.seek(0)  # Retorna ao início do arquivo
    print(arquivo.read())  # Imprime o conteúdo novamente
# Abre o arquivo para escrita, acrescenta uma nova linha e fecha
with open('novo_arquivo.txt', 'a') as arquivo:
    arquivo.write('\nNunca é demais')

# Reabre o arquivo para leitura
with open('novo_arquivo.txt', 'r') as arquivo:
    print(arquivo.read())  # Imprime o conteúdo do arquivo
f = open("novo_arquivo.txt", "r")
for linha in f:
 print(linha)
f.seek(0)
for linha in f:
 print(linha, end='')
# Função para pedir o nome do usuário e gravá-lo em um arquivo de texto
def gravar_nome():
    nome = input("Digite seu nome: ")
    with open("nome_usuario.txt", "w") as arquivo:
        arquivo.write(nome)

# Função para pedir o nome de um arquivo de texto e imprimir seu conteúdo
def imprimir_conteudo():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# Função para ler o conteúdo de um arquivo de exemplo e escrevê-lo em um novo arquivo
def copiar_arquivo():
    with open("exemplo.txt", "r") as arquivo_origem:
        conteudo = arquivo_origem.read()
    with open("novo_arquivo.txt", "w") as arquivo_destino:
        arquivo_destino.write(conteudo)

# Função para pedir um número ao usuário e imprimir o nome correspondente no arquivo de exemplo
def imprimir_nome_por_numero():
    numero = int(input("Digite um número: "))
    with open("exemplo.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        nome = linhas[numero - 1].strip()  # -1 porque os índices começam em 0
        print(nome)

# Exemplo de uso das funções
gravar_nome()
imprimir_conteudo()
copiar_arquivo()
imprimir_nome_por_numero()
