# Questão 1
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)

# Questão 2
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Questão 3
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# Questão 4
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Questão 5
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome}")

# Questão 6
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

# Questão 7
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

#Questão 8
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

# Questão 9
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Questão 10
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)
