#Questão 1
def verificar_colisao(valores, tabela_size):
    tabela = [None] * tabela_size
    colisao = False

    for valor in valores:
        indice = valor % tabela_size
        if tabela[indice] is not None:
            colisao = True
            print(f"Colisão detectada para o valor {valor} no índice {indice}")
        tabela[indice] = valor
    
    if not colisao:
        print("Não houve colisões.")

valores = [120, 123, 145, 90, 39, 45, 23, 220]
tabela_size = 10  
verificar_colisao(valores, tabela_size)

#Questão 2
def calcular_indice(valor, tabela_size):
    return valor % tabela_size

valor = 145
tabela_size = 10
indice = calcular_indice(valor, tabela_size)
print(f"O índice de {valor} na tabela hash de tamanho {tabela_size} é {indice}")

#Questão 3
def verificar_colisao_characters(valores, tabela_size):
    tabela = [None] * tabela_size
    colisao = False

    for valor in valores:
        codigo_ascii = ord(valor)  
        indice = codigo_ascii % tabela_size
        if tabela[indice] is not None:
            colisao = True
            print(f"Colisão detectada para o caractere {valor} ({codigo_ascii}) no índice {indice}")
        tabela[indice] = valor
    
    if not colisao:
        print("Não houve colisões.")

valores = ['U', 'N', 'I', 'E', 'S', 'P', 'F', 'A', 'C', 'U', 'L', 'D', 'A', 'D', 'E']
tabela_size = 10
verificar_colisao_characters(valores, tabela_size)

#Questão 4
def tabela_hash(valores, tabela_size):
    tabela = [[] for _ in range(tabela_size)]

    for valor in valores:
        indice = valor % tabela_size
        tabela[indice].append(valor)
    
    for i, lista in enumerate(tabela):
        print(f"Índice {i}: {lista}")

valores = [2341, 4234, 2839, 430, 22, 397, 3920]
tabela_size = 7
tabela_hash(valores, tabela_size)

#Questão 5
def tabela_hash_sequencial(chaves, tabela_size):
    tabela = [None] * tabela_size

    for chave in chaves:
        indice = chave % tabela_size
        if tabela[indice] is None:
            tabela[indice] = chave
        else:
            if isinstance(tabela[indice], list):
                tabela[indice].append(chave)
            else:
                tabela[indice] = [tabela[indice], chave]
    
    for i, valor in enumerate(tabela):
        print(f"Índice {i}: {valor}")

chaves = [2, 32, 43, 16, 77, 51, 1, 17, 42, 111]
tabela_size = 17
tabela_hash_sequencial(chaves, tabela_size)

#Questão 6
def tabela_hash_customizada(chaves, tabela_size):
    tabela = [None] * tabela_size

    for chave in chaves:
        indice = (2 * chave + 5) % tabela_size
        if tabela[indice] is None:
            tabela[indice] = chave
        else:
            if isinstance(tabela[indice], list):
                tabela[indice].append(chave)
            else:
                tabela[indice] = [tabela[indice], chave]
    
    for i, valor in enumerate(tabela):
        print(f"Índice {i}: {valor}")

chaves = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
tabela_size = 11
tabela_hash_customizada(chaves, tabela_size)
