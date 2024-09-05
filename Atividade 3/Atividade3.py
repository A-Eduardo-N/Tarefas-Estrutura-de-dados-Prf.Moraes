import numpy as np

class Listasequencial:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

  #Questão 1
def maior_numero(lista):
    return max(lista)

# Exemplo de uso
lista = [5, 10, 3, 8, 7]
print("O maior número da lista é:", maior_numero(lista))

#Questão 2
def contar_nomes(nomes):
    return len(nomes)

# Exemplo de uso
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print("Número total de nomes na lista é:", contar_nomes(nomes))

#questão 3
def soma_numeros(lista):
    return sum(lista)

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
print("A soma de todos os números da lista é:", soma_numeros(lista))

#Questão 4
def media_numeros(lista):
    return sum(lista) / len(lista)

# Exemplo de uso
lista = [10, 20, 30, 40, 50]
print("A média dos números da lista é:", media_numeros(lista))

#Questão 5
def contar_palavras_com_a(palavras):
    return sum(1 for palavra in palavras if palavra.lower().startswith('a'))

# Exemplo de uso
palavras = ["Ana", "Pedro", "Alice", "João"]
print("Número de palavras que começam com 'A':", contar_palavras_com_a(palavras))

#Questão 6
def palavra_mais_longa(palavras):
    return max(palavras, key=len)

# Exemplo de uso
palavras = ["banana", "cabelos", "abacaxi", "amendoim"]
print("A palavra mais longa é:", palavra_mais_longa(palavras))

#Questão 7
def listar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso
lista = [1, 2, 3, 4, 5, 6]
print("Números pares:", listar_pares(lista))

#Questão 8
def listar_impares(lista):
    return [num for num in lista if num % 2 != 0]

# Exemplo de uso
lista = [1, 2, 3, 4, 5, 6]
print("Números ímpares:", listar_impares(lista))

#Questão 9
def numeros_comuns(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("Números presentes em ambas as listas:", numeros_comuns(lista1, lista2))

#Questão 10
def remover_repetidos(lista):
    return list(set(lista))

# Exemplo de uso
lista = [1, 2, 3, 2, 4, 1, 5]
print("Lista após remover números repetidos:", remover_repetidos(lista))
