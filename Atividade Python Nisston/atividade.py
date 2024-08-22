#questão 1

print("Digite três números para calcular a média:")


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"A média dos números é: {media}")

#questão 2
def verificar_par_ou_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

verificar_par_ou_impar()
#questão 3
def imprimir_pares():
    limite = int(input("Digite um número: "))
    print("Números pares de 0 até", limite, ":")
    for i in range(limite + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()

imprimir_pares()
#questão 4
def maior_e_menor_lista():
    numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
    else:
        print("A lista está vazia.")

maior_e_menor_lista()
#questão 5
def media_pares_lista():
    numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
    pares = [num for num in numeros if num % 2 == 0]
    if pares:
        media = sum(pares) / len(pares)
        print(f"Média dos números pares: {media}")
    else:
        print("Não há números pares na lista.")

media_pares_lista()
#questão 6
def calcular_fatorial():
    import math
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Número deve ser positivo.")
    else:
        fatorial = math.factorial(numero)
        print(f"O fatorial de {numero} é {fatorial}.")

calcular_fatorial()
#questão 7
def fibonacci_ate_numero():
    limite = int(input("Digite o valor máximo para a sequência de Fibonacci: "))
    a, b = 0, 1
    print("Sequência de Fibonacci:")
    while a <= limite:
        print(a, end=' ')
        a, b = b, a + b
    print()

fibonacci_ate_numero()
#questão 8
def verificar_primo():
    numero = int(input("Digite um número: "))
    if numero <= 1:
        print("O número não é primo.")
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                print("O número não é primo.")
                break
        else:
            print("O número é primo.")

verificar_primo()
#questão 9
def nomes_comeca_com_a():
    nomes = input("Digite uma lista de nomes separados por espaço: ").split()
    nomes_a = [nome for nome in nomes if nome.startswith('A')]
    print("Nomes que começam com 'A':", nomes_a)

nomes_comeca_com_a()
#questão 10
import random

def jogar_pedra_papel_tesoura():
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    if escolha_usuario not in escolhas:
        print("Escolha inválida.")
        return
    escolha_computador = random.choice(escolhas)
    print(f"Computador escolheu: {escolha_computador}")
    
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

jogar_pedra_papel_tesoura()
